package main

import (
	"fmt"
	"os"

	"github.com/gerrowadat/adventofcode/aocutil"
)

type Point struct {
	y, x int
}

// 1:north 2:east 3:south 4:west
type Facing int

type Guard struct {
	pos    Point
	facing Facing
}

type Turn struct {
	pos        Point
	new_facing Facing
}

type Map struct {
	grid    [][]rune
	g       Guard
	visited []Point
	turns   []Turn
	// The added obstacle
	obstacle Point
}

func NewMap(r [][]rune) Map {
	// copy the grid, populatethe Guard struct
	grid := make([][]rune, len(r))
	for i := 0; i < len(r); i++ {
		grid[i] = append([]rune(nil), r[i]...)
	}

	ret := Map{grid: grid}
	ret.Reset()
	return ret
}

func (m *Map) FindGuard() Guard {
	ret := Guard{}
	for i := 0; i < len(m.grid); i++ {
		for j := 0; j < len(m.grid[0]); j++ {
			if m.grid[i][j] == '^' {
				ret.pos = Point{y: i, x: j}
				// guards always face north (for now)
				ret.facing = 1
			}
		}
	}
	m.g = ret
	return ret
}

func (m *Map) Reset() {
	m.FindGuard()
	m.Visit(m.g.pos)
	m.turns = []Turn{}
	m.obstacle = Point{}
}

func (m *Map) String() string {
	ret := ""
	for i := 0; i < len(m.grid); i++ {
		for j := 0; j < len(m.grid[0]); j++ {
			if m.g.pos.x == j && m.g.pos.y == i {
				ret += fmt.Sprintf("%d", m.g.facing)
			} else {
				ret += string(m.grid[i][j])
			}
		}
		ret += "\n"
	}
	return ret
}

func (m *Map) Visit(p Point) {
	for i := range m.visited {
		if m.visited[i].x == p.x && m.visited[i].y == p.y {
			return
		}
	}
	m.visited = append(m.visited, p)
}

func (m *Map) NextRune() rune {
	// Return the rune in front of the guard (or 0 if the edge)
	p := m.NextPoint()
	if p.x == m.obstacle.x && p.y == m.obstacle.y {
		return '#'
	}
	return m.grid[p.y][p.x]
}

func (m *Map) NextPoint() *Point {
	ret := Point{}

	if m.GuardExiting() {
		return nil
	}
	switch m.g.facing {
	case 1:
		ret.x = m.g.pos.x
		ret.y = m.g.pos.y - 1
	case 2:
		ret.x = m.g.pos.x + 1
		ret.y = m.g.pos.y
	case 3:
		ret.x = m.g.pos.x
		ret.y = m.g.pos.y + 1
	case 4:
		ret.x = m.g.pos.x - 1
		ret.y = m.g.pos.y
	}
	return &ret
}

func (m *Map) MoveGuard() {
	// We assume we've checked for an obstacle last time.

	// First, do the actual move.
	switch m.g.facing {
	case 1:
		m.g.pos.y -= 1
	case 2:
		m.g.pos.x += 1
	case 3:
		m.g.pos.y += 1
	case 4:
		m.g.pos.x -= 1
	}

	// Last, switch facing if we're facing an obstacle.
	if !m.GuardExiting() {
		turning := false
		for m.NextRune() == '#' {
			turning = true
			if m.g.facing == 4 {
				m.g.facing = 1
			} else {
				m.g.facing++
			}
		}
		if turning {
			// Store our facing
			turn := Turn{pos: Point{y: m.g.pos.y, x: m.g.pos.x}, new_facing: m.g.facing}
			m.turns = append(m.turns, turn)
		}
	}

	// Mark our new location as visited
	m.Visit(m.g.pos)
}

func (m *Map) Looping() bool {
	// Find a past occurance of our most recent turn, and see if there's a loop since we were last here.
	loopturns := []int{}
	last := m.turns[len(m.turns)-1]
	for i := 0; i < len(m.turns); i++ {
		if m.turns[i].pos.x == last.pos.x && m.turns[i].pos.y == last.pos.y && m.turns[i].new_facing == last.new_facing {
			loopturns = append(loopturns, i)
		}
	}

	if len(loopturns) < 3 {
		return false
	}

	//loop1 := m.turns[loopturns[len(loopturns)-2]:loopturns[len(loopturns)-1]]
	loop1 := m.turns[loopturns[len(loopturns)-2]:]
	loop2 := m.turns[loopturns[len(loopturns)-3] : loopturns[len(loopturns)-2]+1]

	if len(loop1) != len(loop2) {
		return false
	}

	loopmatch := true
	for i := 0; i < len(loop1); i++ {
		if loop1[i].pos.x != loop2[i].pos.x || loop1[i].pos.y != loop2[i].pos.y || loop1[i].new_facing != loop2[i].new_facing {
			loopmatch = false
		}
	}
	/*
		if loopmatch {
			fmt.Printf("Loop size of %d found on turn %v (%v) [turns: %v]\n", len(loop1)-1, last, loop1, loopturns)
		}
	*/

	return loopmatch
}

func (m *Map) GuardExiting() bool {
	// return true if guard is about to exit.
	switch m.g.facing {
	case 1:
		if m.g.pos.y == 0 {
			return true
		}
	case 2:
		if m.g.pos.x == (len(m.grid[0]) - 1) {
			return true
		}
	case 3:
		if m.g.pos.y == (len(m.grid) - 1) {
			return true
		}
	case 4:
		if m.g.pos.x == 0 {
			return true
		}
	}
	return false
}

func (m *Map) NewObstacleLoops(itercount int) bool {
	for i := 0; i < itercount; i++ {
		if m.GuardExiting() {
			return false
		}
		m.MoveGuard()
	}
	return m.Looping()
}

func FindLoopingObstacles(r [][]rune) []Point {
	// Post-note: It's more efficient to track duplicate turns as we go and halt when we hit a loop,
	// but here we all are.
	m := NewMap(r)

	ret := []Point{}
	for y := 0; y < len(m.grid); y++ {
		for x := 0; x < len(m.grid[0]); x++ {
			if m.grid[y][x] == '.' {
				// Reset the Map, run 100 iterations, see if there's a loop.
				m.Reset()
				m.obstacle = Point{y: y, x: x}
				if m.NewObstacleLoops(1000) {
					ret = append(ret, Point{x: x, y: y})
				}
			}
		}
	}
	return ret
}

func main() {
	fmt.Println("Hello.")
	runes, err := aocutil.GetRuneMatrixFromFile(os.Args[1])
	if err != nil {
		fmt.Println("Read file: ", err)
		os.Exit(1)
	}
	m := NewMap(runes)

	fmt.Printf("Grid Dimensions %dx%d, Guard found at [%d,%d] with facing %d\n", len(m.grid), len(m.grid[0]), m.g.pos.y, m.g.pos.x, m.g.facing)

	for !m.GuardExiting() {
		m.MoveGuard()
	}

	fmt.Println("Part 1: ", len(m.visited))

	loop_points := FindLoopingObstacles(runes)

	fmt.Printf("Part 2: %d\n", len(loop_points))
}

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
}

func NewMap(r [][]rune) Map {
	// copy the grid, populatethe Guard struct
	var g Guard
	grid := make([][]rune, len(r))

	for i := 0; i < len(r); i++ {
		grid[i] = append([]rune(nil), r[i]...)
		for j := 0; j < len(r[0]); j++ {
			if r[i][j] == '^' {
				g.pos = Point{y: i, x: j}
				// guards always face north (for now)
				g.facing = 1
			}
		}
	}
	visited := []Point{g.pos}
	return Map{grid: grid, g: g, visited: visited, turns: []Turn{}}
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
	if m.GuardExiting() {
		return 0
	}
	switch m.g.facing {
	case 1:
		return m.grid[m.g.pos.y-1][m.g.pos.x]
	case 2:
		return m.grid[m.g.pos.y][m.g.pos.x+1]
	case 3:
		return m.grid[m.g.pos.y+1][m.g.pos.x]
	case 4:
		return m.grid[m.g.pos.y][m.g.pos.x-1]
	}
	return 0
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
	if !m.GuardExiting() && m.NextRune() == '#' {
		if m.g.facing == 4 {
			m.g.facing = 1
		} else {
			m.g.facing++
		}
		// Store our facing
		turn := Turn{pos: Point{y: m.g.pos.y, x: m.g.pos.x}, new_facing: m.g.facing}
		m.turns = append(m.turns, turn)

	}

	// Mark our new location as visited
	m.Visit(m.g.pos)
}

func (m *Map) Looping() bool {
	// Find a past occurance of our most recent turn, and see if there's a loop since we were last here.
	loopturns := []int{}
	for i := 0; i < len(m.turns); i++ {
		if m.turns[i] == m.turns[len(m.turns)-1] {
			loopturns = append(loopturns, i)
		}
	}

	if len(loopturns) < 3 {
		return false
	}

	loop1 := m.turns[loopturns[len(loopturns)-2]:loopturns[len(loopturns)-1]]
	loop2 := m.turns[loopturns[len(loopturns)-3]:loopturns[len(loopturns)-2]]

	if len(loop1) != len(loop2) {
		return false
	}

	for i := 0; i < len(loop1); i++ {
		if loop1[i].pos.x != loop2[i].pos.x || loop1[i].pos.y != loop2[i].pos.y || loop1[i].new_facing != loop2[i].new_facing {
			return false
		}
	}

	return true
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

func (m *Map) NewObstacleLoops(p Point, itercount int) bool {
	m.grid[p.y][p.x] = '#'
	for i := 0; i < itercount; i++ {
		if m.GuardExiting() {
			m.grid[p.y][p.x] = '.'
			return false
		}
		m.MoveGuard()
	}
	m.grid[p.y][p.x] = '.'
	return m.Looping()
}

func FindLoopingObstacles(r [][]rune) []Point {
	// Post-note: It's more efficient to track duplicate turns as we go and halt when we hit a loop,
	// but here we all are.
	m := NewMap(r)
	g := Guard{pos: Point{x: m.g.pos.x, y: m.g.pos.y}, facing: m.g.facing}

	ret := []Point{}
	for y := 0; y < len(m.grid); y++ {
		for x := 0; x < len(m.grid[0]); x++ {
			if m.grid[y][x] == '.' {
				// Reset the guard, run 100 iterations, see if there's a loop.
				m.g = g
				// Fun note for future Dave, we seem to find fewer loops the more iterations we do, so there's some stupid bug somewhere and maybe someday I'll find it.
				if m.NewObstacleLoops(Point{x: x, y: y}, 100) {
					ret = append(ret, Point{x: x, y: y})
				}
			}
		}
	}
	return ret
}

func main() {
	fmt.Println("Hello.")
	runes, err := aocutil.GetRuneMatrixFromFile("input.txt")
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

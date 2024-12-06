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

type Map struct {
	grid    [][]rune
	g       Guard
	visited []Point
}

func NewMap(r [][]rune) Map {
	// copy the grid, erase the guard rune and move tha tinfo to the Guard struct
	var g Guard
	for i := 0; i < len(r); i++ {
		for j := 0; j < len(r[0]); j++ {
			if r[i][j] == '^' {
				g.pos = Point{y: i, x: j}
				// guards always face north (for now)
				g.facing = 1
				r[i][j] = '.'
			}
		}
	}
	visited := []Point{g.pos}
	return Map{grid: r, g: g, visited: visited}
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
	if m.NextRune() == '#' {
		if m.g.facing == 4 {
			m.g.facing = 1
		} else {
			m.g.facing++
		}
	}

	// Mark our new location as visited
	m.Visit(m.g.pos)
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

func main() {
	fmt.Println("Hello.")
	runes, err := aocutil.GetRuneMatrixFromFile("input.txt")
	if err != nil {
		fmt.Println("Read file: ", err)
		os.Exit(1)
	}
	m := NewMap(runes)

	fmt.Printf("Grid Dimensions %dx%d, Guard found at [%d,%d] with facing %d\n", len(m.grid), len(m.grid[0]), m.g.pos.y, m.g.pos.x, m.g.facing)
	//fmt.Println(m.String())

	for !m.GuardExiting() {
		m.MoveGuard()
	}

	fmt.Println("Part 1: ", len(m.visited))
}

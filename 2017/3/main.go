package main

import (
	"fmt"
	"os"

	"github.com/gerrowadat/adventofcode/aocutil"
)

// Basic SpiralWalker (for part 1)

type SpiralWalker struct {
	// coordinates
	x int
	y int
	// the curent number we've counted out to
	current int
	// the target number of steps
	target int
	// the number of steps to the next 'corner'.
	steps int
	// The number of times we've stepped the current number of steps.
	stepcount int
	// The direction we're currently walking.
	// 0 = right, 1 = up, 2 = left, 3 = down
	dir int
}

func NewSpiralWalker(target int) *SpiralWalker {
	return &SpiralWalker{
		x:         0,
		y:         0,
		current:   1,
		target:    target,
		steps:     1,
		stepcount: 0,
		dir:       0,
	}
}

func (sw *SpiralWalker) Step(steps int) {
	switch sw.dir {
	case 0:
		sw.x += steps
	case 1:
		sw.y += steps
	case 2:
		sw.x -= steps
	case 3:
		sw.y -= steps
	}
}

func (sw *SpiralWalker) Next() bool {
	if sw.current == sw.target {
		return true
	}

	if sw.current+sw.steps > sw.target {
		sw.Step(sw.target - sw.current)
		return true
	}

	sw.Step(sw.steps)
	sw.current += sw.steps
	sw.stepcount++
	if sw.stepcount == 2 {
		sw.stepcount = 0
		sw.steps++
	}

	sw.dir = (sw.dir + 1) % 4

	return false
}

func (sw *SpiralWalker) Walk() {
	// Walk until we get there.
	for !sw.Next() {
	}
}

func ManhattanDistanceFromOrigin(x, y int) int {
	return max(x, -x) + max(y, -y)
}

// A spiralwalker that does a thing (for part 2.)

// But first! The thing.

type GridCoords struct {
	x int
	y int
}

type SpiralGrid map[GridCoords]int

type GridInfillWalker struct {
	SpiralWalker
	grid   SpiralGrid
	result int
}

func (sw *GridInfillWalker) Next() bool {
	// Step the number of steps, filling in the grid as we go.
	all_steps := getAllStepsInLine(sw.x, sw.y, sw.dir, sw.steps)
	for _, step := range all_steps {
		// Get the sum of the surrounding squares.
		sum := 0
		for i := -1; i <= 1; i++ {
			for j := -1; j <= 1; j++ {
				if i == 0 && j == 0 {
					continue
				}
				sum += sw.grid[GridCoords{step.x + i, step.y + j}]
			}
		}
		if sum > sw.target {
			sw.result = sum
			return true
		}
		if !(step.x == 0 && step.y == 0) {
			sw.grid[step] = sum
		}
	}

	sw.Step(sw.steps)
	sw.current += sw.steps
	sw.stepcount++
	if sw.stepcount == 2 {
		sw.stepcount = 0
		sw.steps++
	}

	sw.dir = (sw.dir + 1) % 4

	if sw.grid[GridCoords{sw.x, sw.y}] > sw.target {
		return true
	}

	return false
}

func (sw *GridInfillWalker) Walk() {
	// Walk until we get there.
	for !sw.Next() {
	}
}

func getAllStepsInLine(x, y, dir, steps int) []GridCoords {
	ret := make([]GridCoords, steps)
	for i := 0; i < steps; i++ {
		switch dir {
		case 0:
			ret[i] = GridCoords{x + i, y}
		case 1:
			ret[i] = GridCoords{x, y + i}
		case 2:
			ret[i] = GridCoords{x - i, y}
		case 3:
			ret[i] = GridCoords{x, y - i}
		}
	}
	return ret
}

func main() {
	var input int
	input, err := aocutil.GetFileNumber("input.txt")

	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	fmt.Printf("Input: %d\n", input)

	// There is probably a clever computer person way of doing this thing. I am not that person.
	sw := NewSpiralWalker(input)
	sw.Walk()
	fmt.Printf("Part 1: %d\n", ManhattanDistanceFromOrigin(sw.x, sw.y))

	// Part 2
	grid := make(SpiralGrid)
	grid[GridCoords{0, 0}] = 1
	gw := &GridInfillWalker{
		SpiralWalker: *NewSpiralWalker(input),
		grid:         grid,
	}
	gw.Walk()
	fmt.Printf("Part 2: %d\n", gw.result)

}

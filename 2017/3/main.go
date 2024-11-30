package main

import (
	"fmt"
	"os"

	"github.com/gerrowadat/adventofcode/aocutil"
)

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
	for !sw.Next() {
	}
}

func ManhattanDistanceFromOrigin(x, y int) int {
	return max(x, -x) + max(y, -y)
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
}

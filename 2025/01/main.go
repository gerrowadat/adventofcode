package main

import (
	"fmt"
	"strconv"

	"github.com/gerrowadat/adventofcode/aocutil"
)

type Direction int

const (
	Left Direction = iota
	Right
)

func DecodeStep(step string) (Direction, int) {
	if len(step) == 0 {
		return Left, 0
	}
	lr := step[:1]
	var dir Direction
	if lr == "L" {
		dir = Left
	} else {
		dir = Right
	}
	steps, err := strconv.Atoi(step[1:])
	if err != nil {
		panic(fmt.Errorf("could not parse step count in line [%v]: %v", step, err))
	}
	return dir, steps
}

func ProcessStep(current int, dir Direction, steps int) int {
	ret := 0
	// remove whole wraparounds
	steps = steps % 100
	// wrap around a 0-99 range
	if dir == Left {
		ret = current - steps
		if ret < 0 {
			return 100 + ret
		}
	} else {
		ret = current + steps
		if ret > 99 {
			return ret - 100
		}
	}
	return ret
}

func main() {
	fmt.Println("Hello.")
	lines, err := aocutil.GetFileLines("input.txt")
	if err != nil {
		fmt.Println(err)
		return
	}
	zeroes := 0
	current := 50
	for _, line := range lines {
		dir, steps := DecodeStep(line)
		newPos := ProcessStep(current, dir, steps)
		fmt.Printf("[%v]: From %d to %d\n", line, current, newPos)
		if newPos == 0 {
			zeroes++
		}
		current = newPos
	}
	fmt.Printf("Total zero crossings: %d\n", zeroes)
}

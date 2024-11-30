package main

import (
	"fmt"
	"strconv"

	"github.com/gerrowadat/adventofcode/aocutil"
)

func GetFileLinesAsInts(fileName string) ([]int, error) {
	lines, err := aocutil.GetFileLines(fileName)
	if err != nil {
		return nil, err
	}

	ints := make([]int, len(lines))
	for i, line := range lines {
		ints[i], err = strconv.Atoi(line)
		if err != nil {
			return nil, fmt.Errorf("Non-int on line %d: %v (%v)", i, line, err)
		}
	}
	return ints, nil
}

type Incrementer struct {
	Instructions []int
	Position     int
	StepCount    int
}

func NewIncrementer(instructions []int) *Incrementer {
	return &Incrementer{
		Instructions: instructions,
		Position:     0,
		StepCount:    0,
	}
}

func (c *Incrementer) Run() {
	for c.Position >= 0 && c.Position < len(c.Instructions) {
		c.Step()
	}
}

func (c *Incrementer) Step() {
	c.StepCount++
	instruction := c.Instructions[c.Position]
	c.Instructions[c.Position]++
	c.Position += instruction
}

func (c *Incrementer) String() string {
	return fmt.Sprintf("Cpu{Position: %d, Instructions: %v}", c.Position, c.Instructions)
}

// Part 2 modifications

type Threecrementer struct {
	Instructions []int
	Position     int
	StepCount    int
}

func NewThreecrementer(instructions []int) *Threecrementer {
	return &Threecrementer{
		Instructions: instructions,
		Position:     0,
		StepCount:    0,
	}
}

func (c *Threecrementer) Run() {
	for c.Position >= 0 && c.Position < len(c.Instructions) {
		c.Step()
	}
}

func (c *Threecrementer) Step() {
	c.StepCount++
	instruction := c.Instructions[c.Position]
	if instruction >= 3 {
		c.Instructions[c.Position]--
	} else {
		c.Instructions[c.Position]++
	}
	c.Position += instruction
}

func main() {
	in, err := GetFileLinesAsInts("input.txt")
	if err != nil {
		fmt.Println(err)
		return
	}

	part2 := make([]int, len(in))
	copy(part2, in)

	cpu := NewIncrementer(in)
	cpu.Run()
	fmt.Printf("Part 1: %d\n", cpu.StepCount)

	threecrem := NewThreecrementer(part2)
	threecrem.Run()
	fmt.Printf("Part 2: %d\n", threecrem.StepCount)
}

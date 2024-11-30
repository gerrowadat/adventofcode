package main

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/gerrowadat/adventofcode/aocutil"
)

type Bank struct {
	Blocks int
}

// Part 1

type Mem struct {
	Banks      []Bank
	Observed   [][]int
	CycleCount int
}

func NewMem(banks []int) *Mem {
	mem := &Mem{
		Banks:      make([]Bank, len(banks)),
		Observed:   make([][]int, 0),
		CycleCount: 0,
	}

	for i := 0; i < len(banks); i++ {
		mem.Banks[i].Blocks = banks[i]
	}

	return mem
}

func (m *Mem) String() string {
	return fmt.Sprintf("Mem{Banks: %v, CycleCount: %d}", m.Banks, m.CycleCount)
}

func (m *Mem) Cycle() {
	max := 0
	maxIndex := 0

	for i := 0; i < len(m.Banks); i++ {
		if m.Banks[i].Blocks > max {
			max = m.Banks[i].Blocks
			maxIndex = i
		}
	}

	blocks := m.Banks[maxIndex].Blocks
	m.Banks[maxIndex].Blocks = 0

	for i := 1; i <= blocks; i++ {
		m.Banks[(maxIndex+i)%len(m.Banks)].Blocks++
	}

	// Store our result in observed values.
	observed := make([]int, len(m.Banks))
	for i := 0; i < len(m.Banks); i++ {
		observed[i] = m.Banks[i].Blocks
	}
	m.Observed = append(m.Observed, observed)

	m.CycleCount++
}

func (m *Mem) CycleUntilLoop() {
	for {
		m.Cycle()

		for i := 0; i < len(m.Observed)-1; i++ {
			match := false
			for j := 0; j < len(m.Observed[i]); j++ {
				if m.Observed[i][j] != m.Observed[len(m.Observed)-1][j] {
					match = false
					break
				}
				match = true
			}
			if match {
				return
			}
		}
	}
}

func main() {
	lines, err := aocutil.GetFileLines("input.txt")
	if err != nil {
		fmt.Println(err)
		return
	}

	bankstrings := strings.Split(lines[0], " ")

	banks := make([]int, len(bankstrings))

	for i := 0; i < len(bankstrings); i++ {
		banks[i], err = strconv.Atoi(bankstrings[i])
		if err != nil {
			fmt.Println("Converting input: ", err)
			return
		}
	}

	fmt.Printf("Banks (%d): %v\n", len(banks), banks)

	mem := NewMem(banks)
	mem.CycleUntilLoop()
	fmt.Printf("Part 1: %d\n", mem.CycleCount)

}

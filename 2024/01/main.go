package main

import (
	"fmt"
	"sort"

	"github.com/gerrowadat/adventofcode/aocutil"
)

func main() {
	fmt.Println("Hello.")
	lines, err := aocutil.GetFileLines("input.txt")
	if err != nil {
		fmt.Println(err)
		return
	}
	left := make([]int, len(lines))
	right := make([]int, len(lines))
	for i, line := range lines {
		fmt.Sscanf(line, "%d\t%d", &left[i], &right[i])
	}
	sort.Ints(left)
	sort.Ints(right)

	diff := 0

	for i := 0; i < len(left); i++ {
		if right[i] > left[i] {
			diff += right[i] - left[i]
		} else {
			diff += left[i] - right[i]
		}
	}

	fmt.Println("Part 1: ", diff)
}

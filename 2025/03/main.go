package main

import (
	"fmt"

	"github.com/gerrowadat/adventofcode/aocutil"
)

func MaxLocFromIndexes(nums []int, start int, end int) int {
	max := 0
	loc := 0
	for i := start; i < end; i++ {
		if nums[i] > max {
			max = nums[i]
			loc = i
		}
	}
	return loc
}

func MaxJoltage(batts string) int {
	battnums := []int{}
	for _, b := range batts {
		battnum := int(b - '0')
		battnums = append(battnums, battnum)
	}
	first := MaxLocFromIndexes(battnums, 0, len(battnums)-1)
	last := MaxLocFromIndexes(battnums, first+1, len(battnums))
	return (battnums[first] * 10) + battnums[last]
}

func main() {
	fmt.Println("Hello.")
	lines, err := aocutil.GetFileLines("input.txt")
	if err != nil {
		fmt.Println(err)
		return
	}

	total_joltage := 0
	for _, line := range lines {
		if line == "" {
			continue
		}
		max_joltage := MaxJoltage(line)
		fmt.Printf("Max joltage for line [%v] is %v\n", line, max_joltage)
		total_joltage += max_joltage
	}
	fmt.Printf("Total joltage is %v\n", total_joltage)

}

package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"

	"github.com/gerrowadat/adventofcode/aocutil"
)

func GetIntMatrixFromFile(fn, sep string) ([][]int, error) {
	ret := [][]int{}

	lines, err := aocutil.GetFileLines(fn)
	if err != nil {
		fmt.Println("error reading file: ", err)
		os.Exit(1)
	}

	for _, l := range lines {
		fragments := strings.Split(l, sep)
		row := []int{}
		for _, f := range fragments {
			elem, err := strconv.Atoi(f)
			if err != nil {
				return nil, err
			}
			row = append(row, elem)
		}
		ret = append(ret, row)
	}
	return ret, nil
}

func UnsafeElement(report []int) int {

	ascending := true
	if report[1] < report[0] {
		ascending = false
	}

	for i := range report {
		if i == 0 {
			continue
		}

		diff := max(report[i]-report[i-1], -(report[i] - report[i-1]))
		if diff < 1 || diff > 3 {
			return i
		}

		if (ascending && report[i] < report[i-1]) || (!ascending && report[i] > report[i-1]) {
			// Wrong way
			return i
		}

	}
	// element 0 is always 'safe', so returning 0 means safe.
	return 0
}

func WithoutElem(report []int, elem int) []int {
	partial_report := make([]int, len(report)-1)
	p := 0
	for i := range report {
		if i != elem {
			partial_report[p] = report[i]
			p++
		}
	}
	return partial_report
}

func MostlyUnsafeElement(report []int) int {
	unsafe := UnsafeElement(report)
	if unsafe == 0 {
		return 0
	}

	// Try removing each element in turn to see if we're safe then.
	// I'm going to allow myself one more "This could be smarter, but no YOU shut up"
	// style comment, as a treat.
	for i := range report {
		if UnsafeElement(WithoutElem(report, i)) == 0 {
			return 0
		}
	}

	return unsafe
}

func main() {
	fmt.Println("Hello.")
	reports, err := GetIntMatrixFromFile("input.txt", " ")
	if err != nil {
		fmt.Println("error reading file: ", err)
		os.Exit(1)
	}

	safe_count := 0
	mostlysafe_count := 0
	for _, row := range reports {
		if UnsafeElement(row) == 0 {
			safe_count++
		}
		if MostlyUnsafeElement(row) == 0 {
			mostlysafe_count++
		}
	}

	fmt.Println("Part 1: ", safe_count)
	fmt.Println("Part 2: ", mostlysafe_count)

}

package main

import (
	"fmt"
	"strings"
	"strconv"

	"github.com/gerrowadat/adventofcode/aocutil"
)

type Range struct {
	start, end int
}

func RangeFromString(in string) *Range {
	f := strings.Split(in, "-")
	start, err := strconv.Atoi(f[0])
	if err != nil {
		return nil
	}
	end, err := strconv.Atoi(f[1])
	if err != nil {
		return nil
	}
	return &Range{ start: start, end: end }
}

func (r *Range) InvalidIDs() []int {
	ret := []int{}
	for i := r.start; i <= r.end; i++ {
		istr := strconv.Itoa(i)
		if len(istr) % 2 == 0 {
			if istr[0:len(istr)/2] == istr[len(istr)/2:] {
				ret = append(ret, i)
			}
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

	rangestrs := strings.Split(lines[0], ",")

	invalid_total := 0
	for _, rs := range rangestrs {
		r := RangeFromString(rs)
		for _, inv := range r.InvalidIDs() {
			invalid_total += inv
		}
	}
	fmt.Printf("Part 1: %v\n", invalid_total)

}
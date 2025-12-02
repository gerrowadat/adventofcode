package main

import (
	"fmt"
	"strings"
	"strconv"
	"slices"

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

func (r *Range) SimpleInvalidIDs() []int {
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

func RepeatsFirst(in string, count int) bool {
	if len(in) % count != 0 {
		return false
	}
	for i := 0; i < len(in); i += count {
		end := i + count
		if end > len(in) {
			end = len(in)
		}
		if in[:count] != in[i:end] {
			return false
		}
	}
	return true
}

func (r *Range) SlightlyMoreComplicatedInvalidIDs() []int {
	ret := []int{}
	for i := r.start; i <= r.end; i++ {
		istr := strconv.Itoa(i)

		// Take a slice of size 1 to half the string, see if it repeats.
		for replen := 1; replen <= len(istr)/2; replen++ {
			if RepeatsFirst(istr, replen) {
				if !slices.Contains(ret, i) {
					ret = append(ret, i)
				}
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

	simple_total := 0
	slightlymorecomplicated_total := 0
	for _, rs := range rangestrs {
		r := RangeFromString(rs)
		for _, inv := range r.SimpleInvalidIDs() {
			simple_total += inv
		}
		for _, inv := range r.SlightlyMoreComplicatedInvalidIDs() {
			slightlymorecomplicated_total += inv
		}
	}
	fmt.Printf("Part 1: %v\n", simple_total)
	fmt.Printf("Part 2: %v\n", slightlymorecomplicated_total)

}
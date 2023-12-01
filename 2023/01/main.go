package main

import (
	"fmt"
	"strconv"
)

func numberAtIndex(line string, idx int) int {
	// Return a number 0-9 if it's at index idx of string line
	if line[idx] >= '0' && line[idx] <= '9' {
		return int(line[idx]) - 48
	}
	nums := map[int]string{1: "one",
		2: "two",
		3: "three",
		4: "four",
		5: "five",
		6: "six",
		7: "seven",
		8: "eight",
		9: "nine"}

	for n, str := range nums {
		if len(line) >= idx+len(str) {
			if line[idx:idx+len(str)] == str {
				return n
			}
		}
	}
	return 0
}

func firstlast(line string) int {
	var first, last int
	for i := range line {
		at := numberAtIndex(line, i)
		if at != 0 {
			if first == 0 {
				first = at
			}
			last = at
		}
	}

	flstr := fmt.Sprintf("%d%d", first, last)

	ret, err := strconv.Atoi(flstr)

	if err != nil {
		fmt.Printf("Error converting %s to integer\n", flstr)
	}

	return ret
}

func main() {
	instructions := getFileLines("input.txt")
	tot := 0

	for _, i := range instructions {
		fl := firstlast(i)
		fmt.Printf("%s: %d\n", i, fl)
		tot = tot + fl
	}
	fmt.Printf("Total: %d\n", tot)
}

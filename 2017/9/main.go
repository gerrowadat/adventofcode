package main

import (
	"fmt"
	"os"

	"github.com/gerrowadat/adventofcode/aocutil"
)

func main() {
	fmt.Println("Hello.")
	lines, err := aocutil.GetFileLines("input.txt")
	if err != nil {
		fmt.Println("Reading file")
		os.Exit(1)
	}

	if len(lines) != 1 {
		fmt.Println("not a single line")
		os.Exit(2)
	}

	in := lines[0]

	layer := 0

	score := 0

	garbage := false
	gc := 0

	c := 0

	for {
		if c == len(in)-1 {
			break
		}
		if in[c] == '{' {
			if !garbage {
				layer += 1
				score += layer
			} else {
				gc++
			}
			c++
			continue
		}
		if in[c] == '}' {
			if !garbage {
				layer -= 1
			} else {
				gc++
			}
			c++
			continue
		}
		if in[c] == '<' {
			if garbage {
				gc++
			}
			garbage = true
			c++
			continue
		}
		if in[c] == '>' {
			garbage = false
			c++
			continue
		}
		if in[c] == '!' {
			c += 2
			continue
		}
		if garbage {
			gc++
		}
		c++
	}

	fmt.Println("Part 1: ", score)
	fmt.Println("Part 2: ", gc)
}

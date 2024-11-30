package main

import (
	"fmt"
	"os"
	"strings"

	"github.com/gerrowadat/adventofcode/aocutil"
)

func CanBeAnagram(a, b string) bool {
	if len(a) != len(b) {
		return false
	}

	amap := make(map[rune]int)
	bmap := make(map[rune]int)

	for _, r := range a {
		amap[r]++
	}

	for _, r := range b {
		bmap[r]++
	}

	for k, v := range amap {
		if bmap[k] != v {
			return false
		}
	}

	return true
}

func main() {
	var phrases []string
	phrases, err := aocutil.GetFileLines("input.txt")
	if err != nil {
		fmt.Println("Error reading input file: ", err)
		os.Exit(1)
	}

	validcount := 0

	for _, phrase := range phrases {
		words := strings.Split(phrase, " ")

		// Check for duplicates
		wordmap := make(map[string]bool)
		valid := true
		for _, word := range words {
			if wordmap[word] {
				valid = false
				break
			}
			wordmap[word] = true
		}

		if valid {
			validcount++
		}

	}

	fmt.Println("Part 1: ", validcount)

	validcount = 0

	for _, phrase := range phrases {
		words := strings.Split(phrase, " ")

		// Check for duplicates
		wordmap := make(map[string]bool)
		valid := true
		for _, word := range words {
			for k := range wordmap {
				if CanBeAnagram(k, word) {
					valid = false
					break
				}
			}
			if !valid {
				break
			}
			wordmap[word] = true
		}

		if valid {
			validcount++
		}

	}

	fmt.Println("Part 2: ", validcount)
}

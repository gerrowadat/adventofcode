package main

import (
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"

	"github.com/gerrowadat/adventofcode/aocutil"
)

type rule struct {
	l int
	r int
}

func UpdateFollowsRule(u []int, rl rule) bool {
	l := slices.Index(u, rl.l)
	r := slices.Index(u, rl.r)

	if l == -1 || r == -1 {
		return true
	}

	if l > r {
		return false
	}

	return true
}

func UpdateFollowsRules(u []int, r []rule) bool {

	for i := range r {
		if !UpdateFollowsRule(u, r[i]) {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println("Hello.")
	lines, err := aocutil.GetFileLines("input.txt")
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	rules := []rule{}
	updates := [][]int{}

	for i := range lines {
		ruleparts := strings.Split(lines[i], "|")
		if len(ruleparts) == 2 {
			l, err := strconv.Atoi(ruleparts[0])
			if err != nil {
				fmt.Printf("Line %d: %s\n", i, err)
				os.Exit(2)
			}
			r, err := strconv.Atoi(ruleparts[1])
			if err != nil {
				fmt.Printf("Line %d: %s\n", i, err)
				os.Exit(2)
			}
			rules = append(rules, rule{l, r})
		}
		updateparts := strings.Split(lines[i], ",")
		if len(updateparts) >= 2 {
			partints := []int{}
			for j := range updateparts {
				val, err := strconv.Atoi(updateparts[j])
				if err != nil {
					fmt.Printf("Line %d: %s\n", i, err)
					os.Exit(3)
				}
				partints = append(partints, val)
			}
			updates = append(updates, partints)
		}
	}

	fmt.Printf("Found %d rules and %d updates.\n", len(rules), len(updates))

	middlesum := 0
	for i := range updates {
		if UpdateFollowsRules(updates[i], rules) {
			middlesum += updates[i][len(updates[i])/2]
		}
	}

	fmt.Println("Part 1: ", middlesum)

}

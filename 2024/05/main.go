package main

import (
	"fmt"
	"os"
	"reflect"
	"slices"
	"strconv"
	"strings"

	"github.com/gerrowadat/adventofcode/aocutil"
)

type rule struct {
	l int
	r int
}

type pair [2]int

func UpdateFollowsRule(u []int, rl rule) (bool, pair) {
	l := slices.Index(u, rl.l)
	r := slices.Index(u, rl.r)

	if l == -1 || r == -1 {
		return true, pair{}
	}

	if l > r {
		return false, pair{l, r}
	}

	return true, pair{}
}

func UpdateFollowsRules(u []int, r []rule) bool {

	for i := range r {
		if follows, _ := UpdateFollowsRule(u, r[i]); !follows {
			return false
		}
	}
	return true
}

func DetermineOrder(u []int, r []rule) []int {
	ret := make([]int, len(u))
	copy(ret, u)
	swapE := reflect.Swapper(ret)
	//fmt.Printf("Doing: %v\n", ret)
	// Until we're folowing the rules, iterate through our rules and swap pairs that don't comply.
	for !UpdateFollowsRules(ret, r) {
		for i := range r {
			for {
				f, p := UpdateFollowsRule(ret, r[i])
				if f {
					break
				}
				//fmt.Printf(" - Swapping #%d[%d] and #%d[%d]\n", p[0], ret[p[0]], p[1], ret[p[1]])
				swapE(p[0], p[1])
				//fmt.Printf(" - now [%v]\n", ret)
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

	othermiddlesum := 0
	for i := range updates {
		if !UpdateFollowsRules(updates[i], rules) {
			new_order := DetermineOrder(updates[i], rules)
			othermiddlesum += new_order[len(new_order)/2]
		}
	}

	fmt.Println("Part 2:", othermiddlesum)

}

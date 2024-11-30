package main

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/gerrowadat/adventofcode/aocutil"
)

type Program struct {
	Name     string
	Weight   int
	Children []string
}

func SplitCommaSeparated(in string) []string {
	ret := []string{}
	raw := strings.Split(in, ",")
	for _, r := range raw {
		ret = append(ret, strings.TrimSpace(r))
	}
	return ret
}

func (p *Program) FromString(s string) error {
	// fwft (72) -> ktlj, cntj, xhth
	parts := strings.Split(s, " ")
	if len(parts) < 2 {
		return fmt.Errorf("Invalid program string: %s", s)
	}
	p.Name = parts[0]
	weightParts := strings.Split(parts[1], "(")
	if len(weightParts) < 2 {
		return fmt.Errorf("Invalid program string: %s", s)
	}
	weight, err := strconv.Atoi(strings.TrimRight(weightParts[1], ")"))
	if err != nil {
		return fmt.Errorf("Invalid program string: %s", s)
	}
	p.Weight = weight
	if len(parts) > 2 {
		otherparts := strings.Split(s, "->")
		p.Children = SplitCommaSeparated(otherparts[1])
	}
	return nil
}

func (p *Program) String() string {
	return fmt.Sprintf("%s (%d) -> %v", p.Name, p.Weight, p.Children)
}

func main() {
	fmt.Println("Hello, World!")
	lines, err := aocutil.GetFileLines("input.txt")
	if err != nil {
		fmt.Println(err)
		return
	}

	all_programs := []Program{}
	for _, line := range lines {
		p := Program{}
		err := p.FromString(line)
		if err != nil {
			fmt.Println(err)
			return
		}
		all_programs = append(all_programs, p)
	}
	// Part 1 : find the program with children that doesn't feature in any other program's children.
	// This is some T7-9 tree traversal shit.
	for _, p := range all_programs {
		if len(p.Children) > 0 {
			found := false
			for _, o := range all_programs {
				for _, c := range o.Children {
					if c == p.Name {
						found = true
						break
					}
				}
				if found {
					break
				}
			}
			if !found {
				fmt.Println("Part 1: ", p.Name)
				break
			}
		}
	}
}

package main

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/gerrowadat/adventofcode/aocutil"
)

func SplitCommaSeparated(in string) []string {
	ret := []string{}
	raw := strings.Split(in, ",")
	for _, r := range raw {
		ret = append(ret, strings.TrimSpace(r))
	}
	return ret
}

type Program struct {
	Name        string
	Weight      int
	TotalWeight int
	Children    []string
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

type Tower struct {
	Programs []Program
}

func (t *Tower) AddProgram(p Program) {
	t.Programs = append(t.Programs, p)
}

func (t *Tower) GetProgram(name string) Program {
	for _, p := range t.Programs {
		if p.Name == name {
			return p
		}
	}
	return Program{}
}

func (t *Tower) GetProgramTotalWeight(name string) int {
	// Find the program with the given name, then get the total weight of that program and its children.
	for _, p := range t.Programs {
		if p.Name == name {
			total := p.Weight
			for _, c := range p.Children {
				total += t.GetProgramTotalWeight(c)
			}
			return total
		}
	}
	return 0
}

func (t *Tower) GetRootProgram() Program {
	// Find the program that doesn't feature in any other program's children.
	for _, p := range t.Programs {
		if len(p.Children) > 0 {
			found := false
			for _, o := range t.Programs {
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
				return p
			}
		}
	}
	return Program{}
}

func (t *Tower) FindUnbalancedProgram() Program {
	// Find the program that has children with different weights.
	for _, p := range t.Programs {
		if len(p.Children) > 0 {
			weights := []int{}
			for _, c := range p.Children {
				weights = append(weights, t.GetProgramTotalWeight(c))
			}
			// Check if all the weights are the same.
			weightcounts := map[int]int{}
			for _, w := range weights {
				weightcounts[w]++
			}
			if len(weightcounts) > 1 {
				// Find the program that has the wrong weight.
				// Find the weight that is unique, and find the program that has that weight.
				uniqueWeight := 0
				uniqueProgram := Program{}
				for w, _ := range weightcounts {
					if weightcounts[w] == 1 {
						uniqueWeight = w
					}
					break
				}
				for _, c := range p.Children {
					if t.GetProgramTotalWeight(c) == uniqueWeight {
						uniqueProgram = t.GetProgram(c)
						break
					}
				}
				return uniqueProgram
			}
		}
	}
	return Program{}
}

func (t *Tower) GetExpectedProgramTotalWeight(p Program) int {
	// Find the total weight that the given program should have.
	for _, o := range t.Programs {
		for i, c := range o.Children {
			if c == p.Name {
				// Return the weight of one of the program's siblings.
				return t.GetProgramTotalWeight(o.Children[(i+1)%len(o.Children)])
			}
		}
	}
	return 0
}

func (t *Tower) GetParentProgram(name string) Program {
	// Find the program that has the given program as a child.
	for _, p := range t.Programs {
		for _, c := range p.Children {
			if c == name {
				return p
			}
		}
	}
	return Program{}
}

func main() {
	lines, err := aocutil.GetFileLines("input.txt")
	if err != nil {
		fmt.Println(err)
		return
	}

	t := Tower{}

	for _, line := range lines {
		p := Program{}
		err := p.FromString(line)
		if err != nil {
			fmt.Println(err)
			return
		}
		t.AddProgram(p)
	}

	// Part 1 : find the program with children that doesn't feature in any other program's children.
	// This is some T7-9 tree traversal shit.
	fmt.Println("Part 1: ", t.GetRootProgram().Name)

	// Part 2: Find the one unbalanced program and see what it needs to weigh.
	// Bonus points for avoiding building an actual tree structure at all costs.
	// Extra bonus points because there's a race(?) in here somewhere which means I get an answer only sometimes. Quality.
	unbalanced := t.FindUnbalancedProgram()
	ideal := t.GetExpectedProgramTotalWeight(unbalanced) - (t.GetProgramTotalWeight(unbalanced.Name) - unbalanced.Weight)
	fmt.Printf("Part 2: %s should weigh %d\n", unbalanced.Name, ideal)

}

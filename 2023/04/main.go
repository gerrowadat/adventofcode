package main

import (
	"fmt"
	"strconv"
	"strings"
)

type Card struct {
	id      int
	winners []int
	numbers []int
}

func printCard(c *Card) {
	fmt.Printf("Card %d: ", c.id)
	for _, w := range c.winners {
		fmt.Printf("%d ", w)
	}
	fmt.Printf("| ")
	winnercount := 0
	score := 0
	for _, n := range c.numbers {
		winner := false
		for _, w := range c.winners {
			if n == w {
				winner = true
				winnercount += 1
				if score == 0 {
					score = 1
				} else {
					score = score * 2
				}
			}
		}
		if winner {
			fmt.Printf("[%d] ", n)
		} else {
			fmt.Printf("%d ", n)
		}
	}
	fmt.Printf("= %d (%d winners)\n", score, winnercount)
}

func numstrToIntSlice(raw string) []int {
	ret := []int{}
	for _, nstr := range strings.Fields(raw) {
		n, err := strconv.Atoi(nstr)
		if err != nil {
			fmt.Printf("Funny looking number '%s'\n", nstr)
			return ret
		}
		ret = append(ret, n)
	}
	return ret
}

func parseCard(raw string) *Card {
	ret := &Card{}

	id, err := strconv.Atoi(strings.Fields(strings.Split(raw, ":")[0])[1])
	if err != nil {
		fmt.Printf("Error finding card ID from '%s'\n", raw)
		return ret
	}

	ret.id = id

	winners_str := strings.TrimSpace(strings.Split(strings.Split(raw, ":")[1], "|")[0])
	ret.winners = numstrToIntSlice(winners_str)
	numbers_str := strings.TrimSpace(strings.Split(strings.Split(raw, ":")[1], "|")[1])
	ret.numbers = numstrToIntSlice(numbers_str)

	return ret
}

func scoreCard(c *Card) int {
	ret := 0
	for _, n := range c.numbers {
		for _, w := range c.winners {
			if n == w {
				if ret == 0 {
					ret = 1
				} else {
					ret = ret * 2
				}
			}
		}
	}
	return ret
}

func main() {
	instructions := getFileLines("input.txt")

	cards := []*Card{}

	for _, line := range instructions {
		cards = append(cards, parseCard(line))
	}

	total := 0
	for _, c := range cards {
		total = total + scoreCard(c)
		printCard(c)
	}

	fmt.Printf("Part 1: %d\n", total)
}

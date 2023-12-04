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

func (c *Card) wins() int {
	ret := 0
	for _, n := range c.numbers {
		for _, w := range c.winners {
			if n == w {
				ret++
			}
		}
	}
	return ret
}

func (c *Card) score() int {
	wins := c.wins()
	if wins == 0 {
		return 0
	}
	score := 1
	for i := 0; i < wins-1; i++ {
		score = score * 2
	}
	return score
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
	fmt.Printf("= %d (%d winners)\n", c.score(), c.wins())
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

func recursivePlay(all map[int]*Card, c *Card) int {
	ret := 1

	if c.wins() == 0 {
		return ret
	}

	for i := 1; i <= c.wins(); i++ {
		ret += recursivePlay(all, all[c.id+i])
	}

	return ret
}

func main() {
	instructions := getFileLines("input.txt")

	//cards := []*Card{}
	cards := map[int]*Card{}

	for _, line := range instructions {
		c := parseCard(line)
		cards[c.id] = c
	}

	score_total := 0
	play_total := 0
	for _, c := range cards {
		score_total = score_total + c.score()
		play_total = play_total + recursivePlay(cards, c)
		printCard(c)
	}

	fmt.Printf("Part 1: %d\n", score_total)
	fmt.Printf("Part 2: %d\n", play_total)

}

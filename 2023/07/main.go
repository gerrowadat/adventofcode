package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
)

type Card struct {
	value int
}

func (c *Card) to_string() string {
	switch c.value {
	case 14:
		return "A"
	case 13:
		return "K"
	case 12:
		return "Q"
	case 11:
		return "J"
	case 10:
		return "T"
	default:
		return fmt.Sprintf("%d", c.value)
	}
}

func cardFromByte(b byte) *Card {
	ret := &Card{}
	switch b {
	case 'A':
		ret.value = 14
	case 'K':
		ret.value = 13
	case 'Q':
		ret.value = 12
	case 'J':
		ret.value = 11
	case 'T':
		ret.value = 10
	default:
		ret.value = int(b) - 48
	}
	return ret
}

type Hand struct {
	cards []*Card
	bid   int
}

func (h *Hand) to_string() string {
	ret := ""
	for i := range h.cards {
		ret += h.cards[i].to_string()
	}
	ret += ": " + fmt.Sprintf("%d", h.bid)
	return ret
}

func (h *Hand) unique_cards() []*Card {
	ret := []*Card{}
	for i := range h.cards {
		found := false
		for j := range ret {
			if h.cards[i].value == ret[j].value {
				found = true
			}
		}
		if !found {
			ret = append(ret, h.cards[i])
		}
	}
	return ret
}

func (h *Hand) countMap() map[int][]*Card {
	ret := map[int][]*Card{5: {}, 4: {}, 3: {}, 2: {}, 1: {}}

	uniq := h.unique_cards()
	for i := range uniq {
		count := 0
		for j := range h.cards {
			if h.cards[j].value == uniq[i].value {
				count++
			}
		}
		ret[count] = append(ret[count], uniq[i])
	}
	return ret
}

var handscores = map[string]int{
	"high":      0,
	"pair":      1,
	"2pair":     2,
	"3kind":     3,
	"fullhouse": 4,
	"4kind":     5,
	"5kind":     6,
}

func scoreString(s int) string {
	for k, v := range handscores {
		if v == s {
			return k
		}
	}
	return "unknown"
}

func (h *Hand) handscore() int {
	hmap := h.countMap()
	if len(hmap[5]) != 0 {
		return handscores["5kind"]
	}
	if len(hmap[4]) != 0 {
		return handscores["4kind"]
	}
	if len(hmap[3]) != 0 {
		if len(hmap[2]) != 0 {
			return handscores["fullhouse"]
		}
		return handscores["3kind"]
	}
	if len(hmap[2]) == 2 {
		return handscores["2pair"]
	}
	if len(hmap[2]) == 1 {
		return handscores["pair"]
	}
	if len(hmap[1]) == 5 {
		return handscores["high"]

	}
	// shouldn't get here.

	return -1
}

func (h *Hand) highercardsthan(o *Hand) bool {
	for i := range h.cards {
		if h.cards[i].value == o.cards[i].value {
			continue
		}
		if h.cards[i].value > o.cards[i].value {
			return true
		} else {
			return false
		}
	}
	return false
}

func (h *Hand) beats(o *Hand) bool {
	if h.handscore() > o.handscore() {
		return true
	} else if h.handscore() == o.handscore() {
		if h.highercardsthan(o) {
			return true
		}
	}

	return false
}

func cardsFromString(s string) []*Card {
	ret := []*Card{}
	for i := 0; i < len(s); i++ {
		ret = append(ret, cardFromByte(s[i]))
	}
	return ret
}

func main() {
	lines := getFileLines("input.txt")

	hands := []*Hand{}

	for _, l := range lines {
		fields := strings.Fields(l)
		bid, err := strconv.Atoi(fields[1])
		if err != nil {
			fmt.Printf("Funny-looking bid '%s'", fields[1])
		}
		hands = append(hands, &Hand{bid: bid, cards: cardsFromString(fields[0])})
	}

	sort.Slice(hands, func(i, j int) bool {
		return hands[j].beats(hands[i])
	})

	rank := 1
	total := 0
	for i := range hands {
		winnings := hands[i].bid * rank
		fmt.Printf("rank %d\t: %s (score %s) winnings %d\n", rank, hands[i].to_string(), scoreString(hands[i].handscore()), winnings)
		rank += 1
		total += winnings
	}

	fmt.Printf("Part 1: %d\n", total)

}

package main

import (
	"fmt"
	"strconv"
	"strings"
)

type Race struct {
	duration, record, ways int
}

func (r *Race) attempt(push_duration int) int {
	// Return result of attempt at race after pushing for push_durection ms.
	ret := (push_duration * (r.duration - push_duration))
	return ret
}

func getErrorMargin(r *Race) int {
	ret := 0
	for i := 1; i < r.duration; i++ {
		if r.attempt(i) > r.record {
			ret++
		}
	}
	return ret
}

func main() {
	lines := getFileLines("input.txt")

	races := []*Race{}

	durations := strings.Fields(strings.Split(lines[0], ":")[1])
	records := strings.Fields(strings.Split(lines[1], ":")[1])

	for i := range durations {
		duration, err := strconv.Atoi(durations[i])
		if err != nil {
			fmt.Printf("Funny-looking duration '%s'\n", durations[i])
			break
		}
		record, err := strconv.Atoi(records[i])
		if err != nil {
			fmt.Printf("Funny-looking record '%s'\n", records[i])
			break
		}
		races = append(races, &Race{duration: duration, record: record})
	}

	mult := 1
	for _, r := range races {
		r.ways = getErrorMargin(r)
		mult = mult * r.ways
	}

	fmt.Printf("Part 1: %d\n", mult)

	single_duration, err := strconv.Atoi(strings.Replace(strings.Split(lines[0], ":")[1], " ", "", -1))
	if err != nil {
		fmt.Printf("Funny-looking duration '%s'\n", lines[0])
		return
	}
	single_record, err := strconv.Atoi(strings.Replace(strings.Split(lines[1], ":")[1], " ", "", -1))
	if err != nil {
		fmt.Printf("Funny-looking record '%s'\n", lines[1])
		return
	}

	big_race := &Race{duration: single_duration, record: single_record}

	fmt.Printf("Part 2: %d\n", getErrorMargin(big_race))

}

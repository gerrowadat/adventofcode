package main

import (
	"fmt"
	"strconv"
	"strings"
)

type CubeSet struct {
	colour string
	count  int
}

func getGameInfo(raw_info string) (int, [][]*CubeSet) {
	colon_split := strings.Split(raw_info, ":")
	handFuls := [][]*CubeSet{}
	gameNum, err := strconv.Atoi(strings.Split(colon_split[0], " ")[1])
	if err != nil {
		fmt.Println("Funny-looking game number: ", gameNum)
	}

	handful_split := strings.Split(colon_split[1], ";")

	for i := range handful_split {
		cubesets := []*CubeSet{}

		set_split := strings.Split(handful_split[i], ", ")

		for _, spec := range set_split {
			spec = strings.TrimSpace(spec)
			spec_split := strings.Split(spec, " ")
			count, _ := strconv.Atoi(spec_split[0])
			cubesets = append(cubesets, &CubeSet{colour: spec_split[1], count: count})
		}
		handFuls = append(handFuls, cubesets)
	}

	return gameNum, handFuls
}

func main() {
	instructions := getFileLines("input.txt")

	possibleCount := 0

	cubeCounts := map[string]int{
		"red":   12,
		"green": 13,
		"blue":  14,
	}

	for i := range instructions {
		gameNum, handFuls := getGameInfo(instructions[i])
		fmt.Printf("Game #%d\n", gameNum)
		for i := range handFuls {
			fmt.Printf(" - Handful %d\n", i)
			for _, cs := range handFuls[i] {
				fmt.Printf("   -  %d %s\n", cs.count, cs.colour)
			}
		}
		possible := true
		for _, hf := range handFuls {
			for _, cs := range hf {
				if cs.count > cubeCounts[cs.colour] {
					possible = false
				}
			}
		}
		if possible {
			possibleCount = possibleCount + gameNum
		}
	}
	fmt.Println("Total: ", possibleCount)

}

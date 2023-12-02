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

func gamePower(handfuls [][]*CubeSet) int {
	max := map[string]int{"red": 0, "green": 0, "blue": 0}

	for _, hf := range handfuls {
		for _, cs := range hf {
			if cs.count > max[cs.colour] {
				max[cs.colour] = cs.count
			}

		}
	}
	return max["red"] * max["green"] * max["blue"]
}

func main() {
	instructions := getFileLines("input.txt")

	powerTotal := 0

	for i := range instructions {
		gameNum, handFuls := getGameInfo(instructions[i])
		fmt.Printf("Game #%d\n", gameNum)
		for i := range handFuls {
			fmt.Printf(" - Handful %d\n", i)
			for _, cs := range handFuls[i] {
				fmt.Printf("   -  %d %s\n", cs.count, cs.colour)
			}
		}
		power := gamePower(handFuls)
		fmt.Printf("Game Power: %d\n", power)
		powerTotal = powerTotal + power
	}

	fmt.Printf("Total power: %d\n", powerTotal)

}

package main

import (
	"fmt"
	"os"

	"github.com/gerrowadat/adventofcode/aocutil"
)

func GetRuneMatrixFromFile(fn string) ([][]rune, error) {
	lines, err := aocutil.GetFileLines(fn)
	ret := [][]rune{}
	if err != nil {
		return nil, err
	}
	for _, l := range lines {
		ret = append(ret, []rune(l))
	}
	return ret, nil
}

type point struct {
	x, y int
}

type path struct {
	xinc, yinc int
}

func WordInPath(r [][]rune, w []rune, p point, pa path) bool {
	var check_y, check_x int
	for i := 0; i < len(w); i++ {
		check_y = p.y + (i * pa.yinc)
		check_x = p.x + (i * pa.xinc)

		if check_y >= len(r) || check_x >= len(r[0]) {
			return false
		}

		if check_y < 0 || check_x < 0 {
			return false
		}

		if r[check_y][check_x] != w[i] {
			return false
		}
	}
	return true
}

func WordSearch(r [][]rune, word string, p point) int {
	w := []rune(word)
	if r[p.y][p.x] != w[0] {
		return 0
	}

	match_count := 0
	for i := -1; i < 2; i++ {
		for j := -1; j < 2; j++ {
			if WordInPath(r, w, p, path{i, j}) {
				match_count++
			}
		}
	}

	return match_count
}

func main() {
	fmt.Println("Hello.")

	r, err := GetRuneMatrixFromFile("input.txt")
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	xmascount := 0
	for y := 0; y < len(r); y++ {
		for x := 0; x < len(r[y]); x++ {
			xmascount += WordSearch(r, "XMAS", point{x: x, y: y})
		}
	}
	fmt.Println("Part 1: ", xmascount)
}

package main

import (
	"fmt"
	"os"
	"slices"

	"github.com/gerrowadat/adventofcode/aocutil"
)

type Point struct {
	x, y int
}

type Pair [2]Point

type Antenna struct {
	loc  Point
	freq rune
}

func GetAntennae(g [][]rune) []Antenna {
	ret := []Antenna{}
	for i := range g {
		for j := range g[0] {
			if g[i][j] != '.' {
				ret = append(ret, Antenna{freq: g[i][j], loc: Point{x: j, y: i}})
			}

		}
	}
	return ret
}

func WithinGrid(g [][]rune, p Point) bool {

	return (p.x >= 0 && p.x < len(g[0])) && (p.y >= 0 && p.y < len(g))
}

func GetAntinodesForPair(g [][]rune, p Pair, resonance bool) []Point {
	ret := []Point{}
	ydiff := max(p[0].y-p[1].y, p[1].y-p[0].y)
	xdiff := max(p[0].x-p[1].x, p[1].x-p[0].x)

	var x1, y1, x2, y2 int

	y1 = min(p[0].y, p[1].y) - ydiff
	y2 = max(p[0].y, p[1].y) + ydiff

	if p[0].x < p[1].x {
		x1 = p[0].x - xdiff
		x2 = p[1].x + xdiff
	} else {
		x1 = p[0].x + xdiff
		x2 = p[1].x - xdiff
	}

	possibles := []Point{
		{x: x1, y: y1},
		{x: x2, y: y2},
	}

	for _, poss := range possibles {
		if WithinGrid(g, poss) {
			ret = append(ret, poss)
		}
	}
	return ret
}

func GetPairsForRune(antennae []Antenna, r rune) []Pair {
	ret := []Pair{}
	matchfreq_list := []Antenna{}
	for _, a := range antennae {
		if a.freq == r {
			matchfreq_list = append(matchfreq_list, a)
		}
	}
	for i := 0; i < len(matchfreq_list); i++ {
		for j := i + 1; j < len(matchfreq_list); j++ {
			ret = append(ret, Pair{matchfreq_list[i].loc, matchfreq_list[j].loc})
		}
	}
	return ret
}

func GetPairs(antennae []Antenna) []Pair {
	ret := []Pair{}
	seen := []rune{}
	for _, a := range antennae {
		if slices.Index(seen, a.freq) == -1 {
			ret = append(ret, GetPairsForRune(antennae, a.freq)...)
			seen = append(seen, a.freq)
		}
	}
	return ret
}

func GetAntinodes(g [][]rune, a []Antenna, resonance bool) []Point {
	raw := []Point{}
	for _, pair := range GetPairs(a) {
		raw = append(raw, GetAntinodesForPair(g, pair, resonance)...)
	}
	ret := []Point{}
	// De-duplicate antinodes
	for _, an := range raw {
		if slices.Index(ret, an) == -1 {
			ret = append(ret, an)
		}
	}
	return ret
}

func main() {
	fmt.Println("Hello.")
	grid, err := aocutil.GetRuneMatrixFromFile(os.Args[1])
	if err != nil {
		fmt.Println("opening file: ", err)
		os.Exit(1)
	}

	a := GetAntennae(grid)

	fmt.Printf("Found %d Antennae.\n", len(a))

	an := GetAntinodes(grid, a, false)
	fmt.Printf("Part 1: %d\n", len(an))

	an = GetAntinodes(grid, a, true)
	fmt.Printf("Part 2: %d\n", len(an))

	//fmt.Println(PrintGrid(grid, an))

}

func PrintGrid(grid [][]rune, an []Point) string {

	for _, aan := range an {
		grid[aan.y][aan.x] = '#'
	}

	gg := ""

	for i := range grid {
		for j := range grid[0] {
			gg += string(grid[i][j])
		}
		gg += "\n"
	}
	return gg

}

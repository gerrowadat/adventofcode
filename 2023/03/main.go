package main

import (
	"fmt"
	"strconv"
)

type Point struct {
	x, y int
}

type Num struct {
	loc *Point
	val int
}

func NumFromString(num string, x, y int) *Num {
	num_val, err := strconv.Atoi(num)
	if err != nil {
		fmt.Printf("%s doesn't look like a number", num)
	}
	new_num := &Num{
		val: num_val,
		loc: &Point{
			x: x - len(num),
			y: y,
		},
	}
	return new_num
}

func getAllNums(grid []string) []*Num {
	ret := []*Num{}

	for y, line := range grid {
		this_num := ""
		for x, ch := range line {
			if ch >= '0' && ch <= '9' {
				this_num = this_num + string(ch)
			} else {
				if len(this_num) > 0 {
					ret = append(ret, NumFromString(this_num, x, y))
					this_num = ""
				}
			}
		}
		// also terminate numbers on the RHS of the grid.
		if len(this_num) > 0 {
			ret = append(ret, NumFromString(this_num, len(line), y))
			this_num = ""
		}
	}
	return ret
}

func isInsideNum(n *Num, x, y int) bool {
	num_len := len(fmt.Sprint(n.val))
	if n.loc.y == y && x >= n.loc.x && x < n.loc.x+num_len {
		return true
	}
	return false
}

func getAdjacentPoints(grid []string, n *Num) []*Point {
	ret := []*Point{}
	num_len := len(fmt.Sprint(n.val))
	for x := max(n.loc.x-1, 0); x < min(n.loc.x+num_len+1, len(grid[0])); x++ {
		for y := max(n.loc.y-1, 0); y <= min(n.loc.y+1, len(grid)-1); y++ {
			if !isInsideNum(n, x, y) {
				ret = append(ret, &Point{x: x, y: y})
			}
		}
	}
	return ret
}

func symbolAdjacent(grid []string, n *Num) bool {
	adj := getAdjacentPoints(grid, n)

	for _, p := range adj {
		if (grid[p.y][p.x] != '.') && (grid[p.y][p.x] < '0' || grid[p.y][p.x] > '9') {
			return true
		}
	}

	return false
}

func main() {
	grid := getFileLines("input.txt")

	all_nums := getAllNums(grid)

	sum := 0

	for _, i := range all_nums {
		if symbolAdjacent(grid, i) {
			sum = sum + i.val
		}
	}
	fmt.Printf("Part 1: %d\n", sum)
}

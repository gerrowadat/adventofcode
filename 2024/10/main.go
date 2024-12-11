package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"

	"github.com/gerrowadat/adventofcode/aocutil"
)

func GetIntMatrixFromFile(fn, sep string) ([][]int, error) {
	ret := [][]int{}

	lines, err := aocutil.GetFileLines(fn)
	if err != nil {
		fmt.Println("error reading file: ", err)
		os.Exit(1)
	}

	for _, l := range lines {
		fragments := strings.Split(l, sep)
		row := []int{}
		for _, f := range fragments {
			if f == "." {
				row = append(row, -1)
			} else {
				elem, err := strconv.Atoi(f)
				if err != nil {
					return nil, err
				}
				row = append(row, elem)
			}
		}
		ret = append(ret, row)
	}
	return ret, nil
}

type Trailhead struct {
	g     [][]int
	start Point
	paths []Path
}

type Point struct {
	x, y int
}

type Path map[int]Point

func (p *Path) String() string {
	ret := ""
	i := 0
	for _, v := range *p {
		ret += fmt.Sprintf("%d[%d,%d] ", i, v.x, v.y)
		i++
	}
	return ret
}

func (p *Path) GridString(gridx, gridy int) string {
	pgrid := [][]int{}
	for range gridy {
		row := []int{}
		for range gridx {
			row = append(row, -1)
		}
		pgrid = append(pgrid, row)
	}

	for k, v := range *p {
		pgrid[v.y][v.x] = k
	}

	ret := ""
	for i := range pgrid {
		for j := range pgrid[i] {
			if pgrid[i][j] == -1 {
				ret += "."
			} else {
				ret += fmt.Sprintf("%d", pgrid[i][j])
			}
		}
		ret += "\n"
	}
	return ret
}

func NewTrailhead(g [][]int, start Point) Trailhead {
	return Trailhead{g: g, start: start, paths: []Path{}}
}

func Neighbours(g [][]int, here Point) []Point {
	// Return all valid on-grid 'neighbours' (udlr, not diagonals)
	ret_candidates := []Point{
		{x: here.x, y: here.y - 1},
		{x: here.x, y: here.y + 1},
		{x: here.x - 1, y: here.y},
		{x: here.x + 1, y: here.y},
	}
	ret := []Point{}
	for _, i := range ret_candidates {
		if i.y >= 0 && i.y < len(g) {
			if i.x >= 0 && i.x < len(g[0]) {
				ret = append(ret, i)
			}
		}
	}

	/*
		for i := here.y - 1; i <= here.y+1; i++ {
			if i >= 0 && i < len(g) {
				for j := here.x - 1; j <= here.x+1; j++ {
					if j >= 0 && j < len(g[0]) {
						ret = append(ret, Point{y: i, x: j})
					}
				}
			}
		}
	*/
	return ret
}

func NextSteps(g [][]int, now Point, target int) []Point {
	// Given a grid, where we are (now), return next steps that have height (target)
	ret := []Point{}

	for _, i := range Neighbours(g, now) {
		if g[i.y][i.x] == target {
			ret = append(ret, i)
		}
	}
	return ret
}

func (h *Trailhead) ExtendTrail(p Path, next int) []Path {
	ret := []Path{}
	if _, ok := p[next-1]; ok {
		// Return all valid paths that include the next step.
		n := NextSteps(h.g, p[next-1], next)
		for _, i := range n {
			new_p := Path{}
			for j := 0; j < next; j++ {
				new_p[j] = p[j]
			}
			new_p[next] = i
			ret = append(ret, new_p)
		}
	}
	return ret
}

func (h *Trailhead) FindTrails() []Path {
	// Determine all paths (including partials).
	h.paths = append(h.paths, Path{0: h.start})
	for i := range 10 {
		var new_p []Path
		for j := range h.paths {
			new_p = append(new_p, h.ExtendTrail(h.paths[j], i)...)
		}
		//fmt.Printf("New paths for %d: %v\n", i, new_p)
		h.paths = append(h.paths, new_p...)
		// Prune older paths
		latest_paths := []Path{}
		for j := range h.paths {
			if _, ok := h.paths[j][i]; ok {
				latest_paths = append(latest_paths, h.paths[j])
			}
		}
		h.paths = latest_paths
		//fmt.Println("Paths: ", h.paths)
	}

	ret := []Path{}
	for i := range h.paths {
		if _, ok := h.paths[i][9]; ok {
			ret = append(ret, h.paths[i])
		}
	}

	return ret
}

func (h *Trailhead) Score() int {
	// Populate the initial paths 0->1
	ends := map[Point]bool{}
	for i := range h.paths {
		ends[h.paths[i][9]] = true
	}
	ret := 0
	for range ends {
		ret++
	}
	return ret
}

func (h *Trailhead) Rating() int {
	return len(h.paths)
}

func main() {
	fmt.Println("Hello.")
	grid, err := GetIntMatrixFromFile(os.Args[1], "")
	if err != nil {
		fmt.Println("opening file: ", err)
		os.Exit(1)
	}

	heads := []Trailhead{}

	for i := range grid {
		for j := range grid[0] {
			if grid[i][j] == 0 {
				heads = append(heads, NewTrailhead(grid, Point{y: i, x: j}))
			}
		}
	}

	fmt.Printf("Found %d trailheads.\n", len(heads))

	for i := range heads {
		heads[i].FindTrails()
		/*
			fmt.Printf("Trailhead start: [%d,%d] (%d paths)\n", heads[i].start.x, heads[i].start.y, len(heads[i].paths))
			for j := range heads[i].paths {
				fmt.Println(heads[i].paths[j].GridString(len(grid[0]), len(grid)))
			}
		*/
	}

	totscore := 0
	totrating := 0

	for i := range heads {
		//fmt.Printf("Head: [%d,%d] %d paths\n", heads[i].start.x, heads[i].start.y, heads[i].Score())
		totscore += heads[i].Score()
		totrating += heads[i].Rating()
	}

	fmt.Println("Part 1: ", totscore)
	fmt.Println("Part 2: ", totrating)

}

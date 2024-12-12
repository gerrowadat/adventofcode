package main

import (
	"fmt"
	"os"

	"github.com/gerrowadat/adventofcode/aocutil"
)

type Point struct {
	x, y int
}

func (p *Point) Equals(pp Point) bool {
	return p.x == pp.x && p.y == pp.y
}

func (p *Point) Neighbours() []Point {
	ret := []Point{}
	for i := p.y - 1; i <= p.y+1; i++ {
		for j := p.x - 1; j <= p.x+1; j++ {
			if p.y != i && p.x != j {
				// Only consider cardinal neighbours for borders (i.e. no diagonals).
				continue
			}
			ret = append(ret, Point{x: j, y: i})
		}
	}
	return ret
}

type Region struct {
	label    rune
	points   map[Point]bool
	gridsize Point
}

func (r *Region) FindPoints(g [][]rune, start Point) {
	r.points[start] = true
	growth := 1

	for growth > 0 {
		//fmt.Println(" - Area Grew by ", growth)
		growth = 0
		a := r.Area()

		for p := range r.points {
			for _, n := range p.Neighbours() {
				//fmt.Println(" - Considering ", n)
				if !r.ContainsPoint(n) {
					if n.y >= 0 && n.y < len(g) {
						if n.x >= 0 && n.x < len(g[0]) {
							if g[n.y][n.x] == r.label {
								r.points[n] = true
							}
						}
					}

				}

			}
		}
		growth = r.Area() - a
	}
}

func (r *Region) ContainsPoint(p Point) bool {
	if _, ok := r.points[p]; ok {
		return true
	}
	return false
}

func (r *Region) Area() int {
	ret := 0
	for range r.points {
		ret++
	}
	return ret
}

func (r *Region) Perimeter(g [][]rune) int {
	ret := 0
	for i := range r.points {
		for _, n := range i.Neighbours() {
			if n.y != i.y && n.x != i.x {
				// Only consider cardinal neighbours for borders (i.e. no diagonals).
				continue
			}
			if (n.y < 0 || n.y >= len(g)) || (n.x < 0 || n.x >= len(g[0])) {
				// Grid-edge border
				ret += 1
				continue
			}
			if g[n.y][n.x] != r.label {
				// Border to other region.
				ret += 1
			}
		}
	}
	return ret
}

func GetContainingRegion(r []Region, p Point) *Region {
	for i := range r {
		if r[i].ContainsPoint(p) {
			return &r[i]
		}
	}
	return nil
}

func main() {
	fmt.Println("Hello.")
	grid, err := aocutil.GetRuneMatrixFromFile(os.Args[1])
	if err != nil {
		fmt.Println("opening file: ", err)
		os.Exit(1)
	}

	regions := []Region{}

	for i := range grid {
		for j := range grid[0] {
			here := Point{y: i, x: j}
			if GetContainingRegion(regions, here) == nil {
				new_r := Region{label: grid[i][j], points: map[Point]bool{}, gridsize: Point{y: len(grid), x: len(grid[0])}}
				new_r.FindPoints(grid, here)
				//fmt.Printf("New Region %s of area %d, permieter %d: %v\n", string(new_r.label), new_r.Area(), new_r.Perimeter(grid), new_r.points)
				regions = append(regions, new_r)
			}
		}
	}

	fmt.Printf("Found %d regions in the %dx%d grid.\n", len(regions), len(grid[0]), len(grid))

	fencing_price := 0
	totarea := 0
	for i := range regions {
		fencing_price += regions[i].Area() * regions[i].Perimeter(grid)
		totarea += regions[i].Area()
	}

	fmt.Printf("Total area of all regions: %d/%d\n", totarea, (len(grid) * len(grid[0])))

	fmt.Println("Part 1: ", fencing_price)

}

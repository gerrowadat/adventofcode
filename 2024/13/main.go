package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"

	"github.com/gerrowadat/adventofcode/aocutil"
)

type Button struct {
	x, y int
}

type Machine struct {
	a, b           Button
	prizex, prizey int
}

func (m *Machine) Win() (int, int) {
	mintokens := 0
	mina := 0
	minb := 0
	for i := 1; i <= 100; i++ {
		if (m.prizex-(i*m.a.x))%m.b.x == 0 {
			if (m.prizey-(i*m.a.y))%m.b.y == 0 {
				// found a solution, check if it's cheapest and not too button-pressy.
				this_a := i
				this_b := (m.prizey - (i * m.a.y)) / m.b.y

				if this_a > 100 || this_b > 100 {
					continue
				}

				// Sometimes the solution is too little button-pressy
				if this_b < 0 {
					continue
				}

				tok := 3*this_a + this_b
				if tok < mintokens || mintokens == 0 {
					mintokens = tok
					mina = this_a
					minb = this_b
				}
			}
		}
	}
	return mina, minb
}

func ParseXY(in string, sep string) (int, int) {
	fragments := strings.Split(in, ", ")

	xstr := strings.Split(fragments[0], sep)[1]
	x, err := strconv.Atoi(xstr)
	if err != nil {
		fmt.Printf("Not an int: %s (in %s)\n", xstr, in)
	}

	ystr := strings.Split(fragments[1], sep)[1]
	y, err := strconv.Atoi(ystr)
	if err != nil {
		fmt.Printf("Not an int: %s (in %s)\n", ystr, in)
	}

	return x, y
}

func ParseLine(l string, name string) (int, int) {
	fragments := strings.Split(l, ": ")
	if fragments[0] != name {
		fmt.Printf("Expected '%s' in : %s", name, l)
		os.Exit(1)
	}

	var x, y int
	if name == "Prize" {
		x, y = ParseXY(fragments[1], "=")
	} else {
		x, y = ParseXY(fragments[1], "+")
	}

	return x, y
}

func main() {
	fmt.Println("Hello.")
	lines, err := aocutil.GetFileLines(os.Args[1])
	if err != nil {
		fmt.Println("opening file: ", err)
		os.Exit(1)
	}

	m := []Machine{}

	i := 0
	for i < len(lines) {
		ax, ay := ParseLine(lines[i], "Button A")
		bx, by := ParseLine(lines[i+1], "Button B")
		px, py := ParseLine(lines[i+2], "Prize")
		m = append(m, Machine{a: Button{x: ax, y: ay}, b: Button{x: bx, y: by}, prizex: px, prizey: py})
		i += 4
	}

	tokens := 0
	for i := range m {
		a, b := m[i].Win()
		if a != 0 || b != 0 {
			fmt.Printf("Prize: [%d, %d], a=%d, b=%d\n", m[i].prizex, m[i].prizey, a, b)
			tokens += 3*a + b
		}
	}

	// This is still incorrect, skipping rest of today as I suspect Part is fuckin full on maths shite.
	fmt.Println("Part 1: ", tokens)

}

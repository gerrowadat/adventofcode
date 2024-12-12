package main

import (
	"fmt"
	"os"
	"strconv"

	"github.com/gerrowadat/adventofcode/aocutil"
)

type Stones struct {
	s          map[int]int
	splitcache map[int][2]int
}

func NewStones(l []int) Stones {
	ret := Stones{s: map[int]int{}, splitcache: map[int][2]int{}}
	for i := range l {
		IncMap(ret.s, l[i], 1)

	}
	return ret
}

func IncMap(s map[int]int, stoneval int, inc int) {
	if _, ok := s[stoneval]; !ok {
		s[stoneval] = inc
	} else {
		s[stoneval] += inc
	}
}

func (s *Stones) Blink() {
	new_s := map[int]int{}
	for k, v := range s.s {
		//fmt.Println(k, v)
		if k == 0 {
			IncMap(new_s, 1, v)
			continue
		}
		if split, ok := s.splitcache[k]; ok {
			IncMap(new_s, split[0], v)
			IncMap(new_s, split[1], v)
			continue
		}
		data_str := fmt.Sprintf("%d", k)
		if len(data_str)%2 == 0 {
			s1, err := strconv.Atoi(data_str[0 : len(data_str)/2])
			if err != nil {
				fmt.Printf("Weird: %s\n", data_str)
				os.Exit(1)
			}
			s2, err := strconv.Atoi(data_str[len(data_str)/2:])
			if err != nil {
				fmt.Printf("Weird: %s\n", data_str)
				os.Exit(1)

			}
			IncMap(new_s, s1, v)
			IncMap(new_s, s2, v)
			s.splitcache[k] = [2]int{s1, s2}
		} else {
			IncMap(new_s, k*2024, v)
		}
	}
	s.s = new_s
}

func (s *Stones) Len() int {
	ret := 0
	for _, v := range s.s {
		ret += v
	}
	return ret
}

func main() {
	fmt.Println("Hello.")
	lines, err := aocutil.GetIntMatrixFromFile(os.Args[1], " ")
	if err != nil {
		fmt.Println("opening file: ", err)
		os.Exit(1)
	}

	s := NewStones(lines[0])

	for range 25 {
		s.Blink()
		//fmt.Println(s.String())
	}
	fmt.Println("Part 1: ", s.Len())

	for range 50 {
		s.Blink()
	}

	fmt.Println("Part 2: ", s.Len())

}

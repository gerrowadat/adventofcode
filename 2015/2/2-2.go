package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
)

func main() {

	all_pkg := getFileLines("input.txt")

	total := 0

	for _, p := range all_pkg {
		dim_strs := strings.Split(p, "x")
		l, _ := strconv.Atoi(dim_strs[0])
		w, _ := strconv.Atoi(dim_strs[1])
		h, _ := strconv.Atoi(dim_strs[2])
		dims := []int{l, w, h}
		sort.Ints(dims)

		total += (2*dims[0] + 2*dims[1]) + (dims[0] * dims[1] * dims[2])

	}

	fmt.Printf("Total: %v\n", total)
}

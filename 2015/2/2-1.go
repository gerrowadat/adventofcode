package main

import (
    "fmt"
    "strconv"
    "strings"
)


func main () {

    all_pkg := getFileLines("input.txt")

    total := 0

    for _, p := range all_pkg {
        dims := strings.Split(p, "x")
        l, _ := strconv.Atoi(dims[0])
        w, _ := strconv.Atoi(dims[1])
        h, _ := strconv.Atoi(dims[2])

        extra := getSmallestSide(l, w, h)

        total += (2*l*w) + (2*w*h) + (2*h*l) + extra

    }

    fmt.Printf("Total: %v\n", total)
}
func getSmallestSide(l int, w int, h int) (int) {
    sides := getSides(l, w, h)
    min := sides[0]
    for i := 1; i < len(sides); i++ {
        if sides[i] < min {
            min = sides[i]
        }
    }
    return min
}

func getSides(l int, w int, h int) ([]int) {
    return []int{ l*w, w*h, h*l }
}

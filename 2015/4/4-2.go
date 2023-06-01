package main

import (
    "fmt"
    "strconv"
    "strings"
)

func main() {

    dup := 0

    for _, spec := range getFileLines("input.txt") {
        ranges := strings.Split(spec, ",")
        if rangePartiallyIncludes(ranges[0], ranges[1]) || rangePartiallyIncludes(ranges[1], ranges[0]) {
            dup += 1
        }
    }
    fmt.Println(dup)
}

func rangePartiallyIncludes(spec1 string, spec2 string) (bool) {
    range1 := strings.Split(spec1, "-")
    range2 := strings.Split(spec2, "-")

    rng1_start, _ := strconv.Atoi(range1[0])
    rng1_end, _ := strconv.Atoi(range1[1])
    rng2_start, _ := strconv.Atoi(range2[0])
    rng2_end, _ := strconv.Atoi(range2[1])

    if ((rng1_start <= rng2_start) && (rng2_start <= rng1_end)) || ((rng1_start <= rng2_end) && (rng2_end <= rng1_end)) {
        return true
    }

    return false
}

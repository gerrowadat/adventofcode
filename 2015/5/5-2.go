package main

import (
    "fmt"
    "strings"
)


func has2Pair(in string) (bool) {
    for idx, _ := range in {
        if idx == len(in) - 1 {
            return false
        }
        // Split on this pair, expect 2 fragements if this is the only example.
        sep := in[idx:idx+2]
        fragments := strings.Split(in, sep)
        if len(fragments) != 2 {
            return true
        }
    }
    return false

}

func hasSandwich(in string) (bool) {
    for idx, _ := range in {
        if idx == len(in) - 2 {
            return false
        }
        if in[idx] == in[idx + 2] {
            return true
        }
    }
    return false
}


func isNice(in string) (bool) {
    if has2Pair(in) && hasSandwich(in) {
            return true
    }
    return false
}


func main() {

    nicecount := 0

    for _ , str := range getFileLines("input.txt") {
        nice := isNice(str)
        if nice {
            nicecount++
        }
        fmt.Println(str, " ", nice)
    }

    fmt.Println(nicecount)
}


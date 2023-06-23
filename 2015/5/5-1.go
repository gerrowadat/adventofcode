package main

import (
    "fmt"
    "strings"
)


func isVowel(c rune) (bool) {
    vowels := []rune{'a', 'e', 'i', 'o', 'u'}
    for _, v := range vowels {
        if c == v {
            return true
        }
    }
    return false
}

func has3Vowels(in string) (bool) {
    vowelcount := 0
    for _, c := range in {
        if isVowel(c) {
            vowelcount++
        }
    }
    if vowelcount >= 3 {
        return true
    }
    return false
}

func hasPair(in string) (bool) {
    for idx, _ := range in {
        if idx == (len(in) -1 ) {
            return false
        }
        if in[idx+1] == in[idx] {
            return true
        }
    }
    return false
}

func noBadSubstr(in string) (bool) {
    bad := []string{"ab", "cd", "pq", "xy"}
    for _, b := range bad {
        if strings.Contains(in, b) {
            return false
        }
    }
    return true
}

func isNice(in string) (bool) {
    if has3Vowels(in) {
        if hasPair(in) {
            if noBadSubstr(in) {
                return true
            }
        }
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


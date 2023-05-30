package main

import (
    "fmt"
)

func main() {
    instructions := getFileLines("input.txt")[0]
    floor := 0

    for _, c := range instructions {
        if c == '(' {
            floor += 1
        }
        if c == ')' {
            floor -= 1
        }
    }

    fmt.Printf("Floor %v\n", floor)
}

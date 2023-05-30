package main

import (
    "fmt"
    "os"
)

func main() {
    instructions := getFileLines("input.txt")[0]
    floor := 0

    for i, c := range instructions {
        if c == '(' {
            floor += 1
        }
        if c == ')' {
            floor -= 1
        }
        if floor == -1 {
            fmt.Printf("Entered basement at position %v\n", i + 1)
            os.Exit(0)
        }
    }
}

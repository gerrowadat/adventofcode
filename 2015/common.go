package main

import (
    "fmt"
    "os"
    "strings"
)

func getFileLines(filename string) ([]string) {
    content, err := os.ReadFile(filename)
    if err != nil {
        fmt.Println("Error reading %v : %v", filename, err)
        os.Exit(1)
    }
    return strings.Split(string(content), "\n")
}

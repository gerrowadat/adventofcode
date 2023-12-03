package main

import (
	"fmt"
	"os"
	"strings"
)

func getFileLines(filename string) []string {
	content, err := os.ReadFile(filename)
	if err != nil {
		fmt.Printf("Error reading %v : %v\n", filename, err)
		os.Exit(1)
	}

	lines := strings.Split(string(content), "\n")
	return lines[:len(lines)-1]

}

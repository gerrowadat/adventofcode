package aocutil

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func GetFileNumber(filename string) (ret int, err error) {
	var content []string
	if content, err = GetFileLines(filename); err != nil {
		return 0, err
	}

	return strconv.Atoi(content[0])
}

func GetFileLines(filename string) (ret []string, err error) {
	var content []byte
	if content, err = os.ReadFile(filename); err != nil {
		return nil, fmt.Errorf("Error reading %v : %v\n", filename, err)
	}

	lines := strings.Split(string(content), "\n")
	return lines[:len(lines)-1], nil
}

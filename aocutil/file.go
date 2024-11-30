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

	if len(content) != 1 {
		return 0, fmt.Errorf("File %v does not contain a single line", filename)
	}

	return strconv.Atoi(content[0])
}

func GetFileLines(filename string) (ret []string, err error) {
	var content []byte
	if content, err = os.ReadFile(filename); err != nil {
		return nil, fmt.Errorf("Error reading %v : %v\n", filename, err)
	}

	return strings.Split(string(content), "\n"), nil
}

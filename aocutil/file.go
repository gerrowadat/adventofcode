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
		return 0, fmt.Errorf("file %v does not contain a single line", filename)
	}

	return strconv.Atoi(content[0])
}

func GetFileLines(filename string) (ret []string, err error) {
	var content []byte
	if content, err = os.ReadFile(filename); err != nil {
		return nil, fmt.Errorf("error reading %v : %v", filename, err)
	}

	return strings.Split(string(content), "\n"), nil
}

func GetFileLinesAsInts(fileName string) ([]int, error) {
	lines, err := GetFileLines(fileName)
	if err != nil {
		return nil, err
	}

	ints := make([]int, len(lines))
	for i, line := range lines {
		ints[i], err = strconv.Atoi(line)
		if err != nil {
			return nil, fmt.Errorf("non-int on line %d: %v (%v)", i, line, err)
		}
	}
	return ints, nil
}

func GetIntMatrixFromFile(fn, sep string) ([][]int, error) {
	ret := [][]int{}

	lines, err := GetFileLines(fn)
	if err != nil {
		fmt.Println("error reading file: ", err)
		os.Exit(1)
	}

	for _, l := range lines {
		fragments := strings.Split(l, sep)
		row := []int{}
		for _, f := range fragments {
			elem, err := strconv.Atoi(f)
			if err != nil {
				return nil, err
			}
			row = append(row, elem)
		}
		ret = append(ret, row)
	}
	return ret, nil
}

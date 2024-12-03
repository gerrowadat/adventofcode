package main

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/gerrowadat/adventofcode/aocutil"
)

type Mul struct {
	l int
	r int
}

func GetOperands(e string) (int, int, error) {
	if len(e) < 5 {
		return 0, 0, fmt.Errorf("not long enough")
	}
	if e[0] != '(' {
		return 0, 0, fmt.Errorf("no open paren")
	}
	closer := strings.Index(e, ")")
	if closer == -1 {
		return 0, 0, fmt.Errorf("no close paren")
	}
	nums := strings.Split(e[1:closer], ",")
	if len(nums) != 2 {
		return 0, 0, fmt.Errorf("not two operands")
	}
	l, err := strconv.Atoi(nums[0])
	if err != nil {
		return 0, 0, fmt.Errorf("bad left operand")
	}
	r, err := strconv.Atoi(nums[1])
	if err != nil {
		return 0, 0, fmt.Errorf("bad right operand")
	}
	return l, r, nil
}

func GetMulExpresions(line string) []Mul {
	ret := []Mul{}
	maybes := strings.Split(line, "mul")
	for i := range maybes {
		l, r, err := GetOperands(maybes[i])
		if err != nil {
			continue
		}
		ret = append(ret, Mul{l, r})
	}
	return ret
}

func EvaluateMulExpression(e Mul) int {
	return e.l * e.r
}

func main() {
	fmt.Println("Hello.")
	lines, err := aocutil.GetFileLines("input.txt")
	if err != nil {
		fmt.Println(err)
		return
	}

	muls := []Mul{}
	for i := range lines {
		muls = append(muls, GetMulExpresions(lines[i])...)
	}

	mul_sum := 0
	for i := range muls {
		mul_sum += EvaluateMulExpression(muls[i])
	}

	fmt.Println("Part 1: ", mul_sum)

}

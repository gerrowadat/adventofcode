package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Mul struct {
	l int
	r int
}

func GetFileToString(filename string) (string, error) {
	var content []byte
	content, err := os.ReadFile(filename)
	if err != nil {
		return "", fmt.Errorf("error reading %v : %v", filename, err)
	}
	return string(content), nil
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

func ConsumeMulExpression(in string) Mul {
	l, r, err := GetOperands(in)
	if err != nil {
		return Mul{}
	}
	return Mul{l, r}
}

func ConsumeExpressions(line string) <-chan Mul {
	ch := make(chan Mul)
	c := 0
	go func(line string) {
		do := true
		defer close(ch)
		for {
			next_do := strings.Index(line[c:], "do()")
			next_dont := strings.Index(line[c:], "don't()")
			next_maybemul := strings.Index(line[c:], "mul(")
			if next_do == -1 && next_dont == -1 && next_maybemul == -1 {
				break
			}
			// Remove -1 from consideration
			nexts := []int{}
			if next_do != -1 {
				nexts = append(nexts, next_do)
			}
			if next_dont != -1 {
				nexts = append(nexts, next_dont)
			}
			if next_maybemul != -1 {
				nexts = append(nexts, next_maybemul)
			}
			next := len(line)
			for i := range nexts {
				if nexts[i] > -1 && nexts[i] < next {
					next = nexts[i]
				}
			}
			switch next {
			case next_do:
				do = true
				c += (next_do + 4)
			case next_dont:
				do = false
				c += (next_dont + 7)
			case next_maybemul:
				if do {
					mul := ConsumeMulExpression(line[c+next_maybemul+3:])
					if mul.l != 0 && mul.r != 0 {
						ch <- mul
					}
				}
				c += (next_maybemul + 4)
			default:
				fmt.Println("Shouldn't be here.")
			}
		}
	}(line)
	return ch
}

func EvaluateMulExpression(e Mul) int {
	return e.l * e.r
}

func main() {
	fmt.Println("Hello.")
	lines, err := GetFileToString("input.txt")
	if err != nil {
		fmt.Println(err)
		return
	}

	mul_sum := 0
	muls := GetMulExpresions(lines)
	for i := range muls {
		mul_sum += EvaluateMulExpression(muls[i])
	}

	fmt.Println("Part 1: ", mul_sum)

	cond_muls := ConsumeExpressions(lines)

	mul_sum = 0
	for m := range cond_muls {
		mul_sum += EvaluateMulExpression(m)
	}

	fmt.Println("Part 2: ", mul_sum)

}

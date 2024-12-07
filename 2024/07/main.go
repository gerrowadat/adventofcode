package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"

	"github.com/gerrowadat/adventofcode/aocutil"
)

type Equation struct {
	result   int
	operands []int
}

type Operation int

const (
	AddOperation Operation = iota
	MultiplyOperation
	ConcatenateOperation
)

func GenerateOperations(ops []Operation, operands int) [][]Operation {
	// Given a list of possible operations and the nuber of operands, retuen
	// a slive of possible operations to use in order
	ret := [][]Operation{}
	if operands == 2 {
		for i := range ops {
			ret = append(ret, []Operation{ops[i]})
		}
		return ret
	}
	for i := range ops {
		subops := GenerateOperations(ops, operands-1)
		for j := range subops {
			ret = append(ret, append(subops[j], ops[i]))
		}
	}
	return ret
}

func NewEquation(spec string) (Equation, error) {
	ret := Equation{result: 0, operands: []int{}}
	specparts := strings.Split(spec, ": ")
	if len(specparts) != 2 {
		return ret, fmt.Errorf("malformed spec: %s", spec)
	}
	var err error
	ret.result, err = strconv.Atoi(specparts[0])
	if err != nil {
		return ret, fmt.Errorf("result %s not an int", specparts[0])
	}
	opstrs := strings.Split(specparts[1], " ")
	for i := range opstrs {
		opint, err := strconv.Atoi(opstrs[i])
		if err != nil {
			return ret, fmt.Errorf("operand not an int: %s", opstrs[i])
		}
		ret.operands = append(ret.operands, opint)
	}

	return ret, nil
}

func Op(l, r int, op Operation) int {
	switch op {
	case AddOperation:
		return l + r
	case MultiplyOperation:
		return l * r
	case ConcatenateOperation:
		concat_str := strconv.Itoa(l) + strconv.Itoa(r)
		concat, err := strconv.Atoi(concat_str)
		if err != nil {
			fmt.Printf("Can't concatenate %d and %d\n", l, r)
			os.Exit(4)
		}
		return concat
	}
	fmt.Printf("Unknown operation %d", op)
	return 0
}

func SolveWithTheseOperators(ops []Operation, nums []int) (int, error) {

	if len(nums) == 2 {
		return Op(nums[0], nums[1], ops[0]), nil
	}
	accum := Op(nums[0], nums[1], ops[0])
	nums[1] = accum
	return SolveWithTheseOperators(ops[1:], nums[1:])
}

func (e *Equation) OpResult(ops []Operation) int {
	// Process the equation with the given operations, returning the result.
	nums := make([]int, len(e.operands))
	copy(nums, e.operands)
	ret, err := SolveWithTheseOperators(ops, nums)
	if err != nil {
		fmt.Println("error solving: ", err)
		os.Exit(3)
	}
	return ret
}

func (e *Equation) IsSoluble(valid_ops []Operation) bool {
	for _, ops := range GenerateOperations(valid_ops, len(e.operands)) {
		if e.OpResult(ops) == e.result {
			return true
		}
	}
	return false
}

func main() {
	fmt.Println("Hello.")
	lines, err := aocutil.GetFileLines(os.Args[1])
	if err != nil {
		fmt.Println("opening file: ", err)
		os.Exit(1)
	}

	eqs := []Equation{}

	for i := range lines {
		eq, err := NewEquation(lines[i])
		if err != nil {
			fmt.Println("error parsing input: ", err)
			os.Exit(2)
		}
		eqs = append(eqs, eq)
	}

	fmt.Printf("Read %d Equations\n", len(eqs))

	testvals := 0
	testvalsiphants := 0
	for _, e := range eqs {
		if e.IsSoluble([]Operation{AddOperation, MultiplyOperation}) {
			testvals += e.result
		}
		if e.IsSoluble([]Operation{AddOperation, MultiplyOperation, ConcatenateOperation}) {
			testvalsiphants += e.result
		}
	}

	fmt.Println("Part 1:", testvals)
	fmt.Println("Part 2:", testvalsiphants)
}

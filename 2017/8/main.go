package main

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/gerrowadat/adventofcode/aocutil"
)

type Registers struct {
	registers   map[string]int
	MaxObserved int
}

func NewRegisters() *Registers {
	return &Registers{
		registers:   make(map[string]int),
		MaxObserved: 0,
	}
}

func (r *Registers) Get(register string) int {
	if _, ok := r.registers[register]; !ok {
		r.registers[register] = 0
	}
	return r.registers[register]
}

func (r *Registers) GetAll() map[string]int {
	return r.registers
}

func (r *Registers) Set(register string, value int) {
	if value > r.MaxObserved {
		r.MaxObserved = value
	}
	r.registers[register] = value
}

func (r *Registers) Inc(register string, value int) {
	r.Set(register, r.registers[register]+value)
}

func (r *Registers) Dec(register string, value int) {
	r.Set(register, r.registers[register]-value)
}

func EvaluateCondition(condition string, reg *Registers) bool {
	fragments := strings.Split(condition, " ")
	if len(fragments) != 3 {
		fmt.Println("Invalid condition:", condition)
		return false
	}

	register := fragments[0]
	operator := fragments[1]
	value, err := strconv.Atoi(fragments[2])
	if err != nil {
		fmt.Println("Invalid value:", fragments[2])
		return false
	}

	reg_value := reg.Get(register)
	switch operator {
	case ">":
		return reg_value > value
	case "<":
		return reg_value < value
	case ">=":
		return reg_value >= value
	case "<=":
		return reg_value <= value
	case "==":
		return reg_value == value
	case "!=":
		return reg_value != value
	default:
		fmt.Println("Invalid operator:", operator)
		return false
	}
}

func ExecuteInstruction(instruction string, reg *Registers) {
	fragments := strings.Split(instruction, " ")
	if len(fragments) != 3 {
		fmt.Println("Invalid instruction:", instruction)
		return
	}

	register := fragments[0]
	operator := fragments[1]
	value, err := strconv.Atoi(fragments[2])
	if err != nil {
		fmt.Println("Invalid value:", fragments[2])
		return
	}

	switch operator {
	case "inc":
		reg.Inc(register, value)
	case "dec":
		reg.Dec(register, value)
	default:
		fmt.Println("Invalid operator:", operator)
	}
}

func main() {
	fmt.Println("Hello, World!")
	lines, err := aocutil.GetFileLines("input.txt")
	if err != nil {
		fmt.Println(err)
		return
	}

	reg := NewRegisters()

	for _, line := range lines {
		fragments := strings.Split(line, " if ")
		if len(fragments) != 2 {
			fmt.Println("Invalid line:", line)
			continue
		}
		if EvaluateCondition(fragments[1], reg) {
			ExecuteInstruction(fragments[0], reg)
		}
	}

	max_reg := 0
	for _, value := range reg.GetAll() {
		if value > max_reg {
			max_reg = value
		}
	}

	fmt.Println("Part 1:", max_reg)
	fmt.Println("Part 2:", reg.MaxObserved)

}

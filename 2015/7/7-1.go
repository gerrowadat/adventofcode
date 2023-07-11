// Doesn't work (yet).
package main

import (
    "fmt"
    "log"
    "strconv"
    "strings"
)

type WireValues map[string]uint16


func assignValue(wires *WireValues, name string, val uint16) {
    fmt.Printf("%s -> %d\n", name, val)
    (*wires)[name] = val
}

func checkWireInput(wires *WireValues, input string) (bool) {
    // returns true if we have a value for the input
    _, ok := (*wires)[input]
    return ok
}

func processInstruction(raw string, wires *WireValues) (bool) {
    // process one instruction, return true if complete, false if missing inputs.
    fragments := strings.Split(raw, " ")

    if len(fragments) == 3 && fragments[1] == "->" {
        val_int, _ := strconv.Atoi(fragments[0])
        assignValue(wires, fragments[2], uint16(val_int))
        return true
    }

    if len(fragments) == 4 {
        if fragments[0] == "NOT" {
            if !checkWireInput(wires, fragments[1]) {
                return false
            }
            assignValue(wires, fragments[3], ^((*wires)[fragments[1]]))
            return true
        }
    }

    if len(fragments) == 5 {

        // We always use fragment 0
        if fragments[0] != "1" && !checkWireInput(wires, fragments[0]) {
            return false
        }

        if fragments[1] == "AND" || fragments[1] == "OR" {
            if !checkWireInput(wires, fragments[2]) {
                return false
            }
        }

        var lhs uint16

        if fragments[0] == "1" {
            lhs = uint16(1)
        } else {
            lhs = (*wires)[fragments[0]]
        }


        if fragments[1] == "AND" {
            assignValue(wires, fragments[4], lhs & (*wires)[fragments[2]])
        } else if fragments[1] == "OR" {
            assignValue(wires, fragments[4], lhs | (*wires)[fragments[2]])
        } else if fragments[1] == "LSHIFT" {
            shiftbits, _ := strconv.Atoi(fragments[2])
            assignValue(wires, fragments[4], lhs << shiftbits)
        } else if fragments[1] == "RSHIFT" {
            shiftbits, _ := strconv.Atoi(fragments[2])
            assignValue(wires, fragments[4], lhs >> shiftbits)
        } else {
            log.Fatal("Unknown instruction: ", raw)
        }
        return true
    }
    log.Fatal("Unknown instruction: ", raw)
    return false
}

func processLines(w *WireValues, lines []string) ([]string) {
    ret := []string{}
    prelen := len(lines)
    for _, l := range lines {
        if processInstruction(l, w) == false {
            ret = append(ret, l)
        }
    }
    fmt.Printf("Processed %d lines\n", prelen - len(ret))
    return ret
}

func main() {

    wires := make(WireValues)

    unprocessed := getFileLines("input.txt")

    for len(unprocessed) > 0 {
        unprocessed = processLines(&wires, unprocessed)
        fmt.Printf("%d unprocessed instructions left\n", len(unprocessed))
    }

    for k, v := range wires {
        fmt.Printf("%s:  %d\n", k, v)
    }
}

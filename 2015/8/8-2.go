// Doesn't work (yet).
package main

import (
    "fmt"
)

func getValueLength(raw string) (int) {
    c := 0
    ret := 0
    for c < len(raw) {
        if len(raw) - c == 1 {
            c += 1
            continue
        }
        if raw[c:c+2] == "\\\"" {
            ret += 1
            c += 2
            continue
        } 
        if raw[c:c+2] == "\\\\" {
            ret += 1
            c += 2
            continue
        }
        if raw[c:c+2] == "\\x" {
            ret += 1
            c += 4
            continue
        }
        if string(raw[c]) != "\"" {
            ret += 1
        }
        c += 1
    }
    return ret
}

func getCodeLength(raw string) (int) {
    c := 0
    ret := 2 // quotes...
    for c < len(raw) {
        if string(raw[c]) == "\"" {
            ret += 2
            c += 1
            continue
        }
        if string(raw[c]) == "\\" {
            ret += 2
            c += 1
            continue
        }
        ret += 1
        c += 1
    }
    return ret
}



func main() {
    unprocessed := getFileLines("input.txt")

    code_len := 0
    value_len := 0

    for _, l := range unprocessed {
        value_len += len(l)
        this_code_len := getCodeLength(l)
        fmt.Printf("%s: %d -> %d\n", l, len(l), this_code_len)
        code_len += this_code_len
    }

    fmt.Printf("Difference: %d\n", code_len - value_len)
}

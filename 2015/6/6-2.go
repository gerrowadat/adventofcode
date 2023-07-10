package main

import (
    "fmt"
    "log"
    "strings"
    "strconv"
)

type Coord struct {
    x, y int
}

type CoordField [1000][1000]int


func getCoordsFromRaw(raw string) (Coord) {
    nums := strings.Split(raw, ",")
    if len(nums) != 2 {
        log.Fatal("Error turning into Coords: " + raw)
    }
    x, _ := strconv.Atoi(nums[0])
    y, _ := strconv.Atoi(nums[1])
    return Coord{x: x, y: y}
}

func getCoordsToUpdate(from Coord, to Coord) ([]Coord) {
    ret := []Coord{}

    for x := from.x; x <= to.x; x++ {
        for y := from.y; y <= to.y; y++ {
            ret = append(ret, Coord{x: x, y: y})
        }
    }

    return ret
}

func toggleLights(l *CoordField, from Coord, to Coord) {
    all_Coords := getCoordsToUpdate(from, to)
    for _, c := range all_Coords {
        l[c.x][c.y] += 2
    }
}

func turnOnLights(l *CoordField, from Coord, to Coord) {
    all_Coords := getCoordsToUpdate(from, to)
    for _, c := range all_Coords {
        l[c.x][c.y] += 1
    }
}

func turnOffLights(l *CoordField, from Coord, to Coord) {
    all_coords := getCoordsToUpdate(from, to)
    for _, c := range all_coords {
        if l[c.x][c.y] > 0 {
            l[c.x][c.y] -= 1
        }
    }
}

func processInstruction(raw string, l *CoordField) {
    fragments := strings.Split(raw, " ")
    if fragments[0] == "toggle" {
        toggleLights(l, getCoordsFromRaw(fragments[1]), getCoordsFromRaw(fragments[3]))
        return
    }
    if fragments[0] == "turn" {
        if fragments[1] == "on" {
            turnOnLights(l, getCoordsFromRaw(fragments[2]), getCoordsFromRaw(fragments[4]))
        }
        if fragments[1] == "off" {
            turnOffLights(l, getCoordsFromRaw(fragments[2]), getCoordsFromRaw(fragments[4]))
        }
        return
    }

    log.Fatal("don't know how to " + fragments[0])
}

func main() {

    lights := CoordField{}

    for i := 0; i < 1000; i++ {
        for j := 0; j < 1000; j++ {
            lights[i][j] = 0
        }
    }
    for _ , str := range getFileLines("input.txt") {
        processInstruction(str, &lights)
    }

    lit := 0

    for l, _ := range lights {
        for w, _ := range lights[l] {
            lit += lights[l][w]
        }
    }

    fmt.Printf("Total Brightness: %d\n", lit)

}

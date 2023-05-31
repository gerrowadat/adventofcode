package main

import (
    "fmt"
)

type visit struct {
    x int
    y int
}

func main() {

    script := getFileLines("input.txt")[0]

    visits := []visit{}

    addVisit(&visits, 0, 0)

    x := 0
    y := 0

    for _, c := range script {
        switch c {
        case '<':
            x -= 1
        case '>':
            x += 1
        case '^':
            y += 1
        case 'v':
            y -= 1
        default:
            fmt.Printf("Not sure about %v in script\n", c)
        }
        addVisit(&visits, x, y)
    }
    fmt.Printf("Visits: %v\n", len(visits))
    fmt.Printf("Unique Visits: %v\n", len(uniqueHouses(visits)))

}


func addVisit(visits *[]visit, x int, y int) {
    *visits = append(*visits, visit{x: x, y: y})
}

func uniqueHouses(visits []visit) ([]visit) {
    uniq := []visit{}
    for _, c := range visits {
        already := false
        for _, e := range uniq {
            if c.x == e.x && c.y == e.y {
                already = true
            }
        }
        if already == false {
            uniq = append(uniq, c)
        }
    }
    return uniq
}

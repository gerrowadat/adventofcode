package main

import (
    "fmt"
)

type loc struct {
    x int
    y int
}

func main() {

    script := getFileLines("input.txt")[0]

    visits := []loc{}

    addVisit(&visits, 0, 0)

    santa := loc{x:0, y:0}
    bot := loc{x:0, y:0}

    for i, c := range script {
        if i % 2 == 0 {
            moveAndVisit(&santa, c, &visits)
        } else {
            moveAndVisit(&bot, c, &visits)
        }
    }
    fmt.Printf("Visits: %v\n", len(visits))
    fmt.Printf("Unique Visits: %v\n", len(uniqueHouses(visits)))

}

func moveAndVisit(current *loc, direction rune, visits *[]loc) {
    switch direction {
    case '<':
        current.x -= 1
    case '>':
        current.x += 1
    case '^':
        current.y += 1
    case 'v':
        current.y -= 1
    default:
        fmt.Printf("Not sure about %v in script\n", direction)
    }
    addVisit(visits, current.x, current.y)
}

func addVisit(visits *[]loc, x int, y int) {
    *visits = append(*visits, loc{x: x, y: y})
}

func uniqueHouses(visits []loc) ([]loc) {
    uniq := []loc{}
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

package main

import (
	"fmt"
	"os"

	"github.com/gerrowadat/adventofcode/aocutil"
)

func LastFilled(b []rune) int {
	for i := len(b) - 1; i >= 0; i-- {
		if b[i] != 46 {
			return i
		}
	}
	return -1
}

func FirstFree(b []rune) int {
	for i := 0; i < len(b); i++ {
		if b[i] == 46 {
			return i
		}
	}
	return -1
}

func DefragBlocks(b []rune) []rune {
	ret := make([]rune, len(b))
	copy(ret, b)
	lf := LastFilled(ret)
	ff := FirstFree(ret)
	for lf > ff {
		//fmt.Printf("Defragging Block %d[%v] into block %d[%v]\n", lf, ret[lf], ff, ret[ff])
		ret[ff] = ret[lf]
		ret[lf] = '.'
		lf = LastFilled(ret)
		ff = FirstFree(ret)
		//fmt.Println(string(ret))
	}
	return ret
}

type Disk struct {
	spec   []int
	blocks []rune
}

func NewDisk(spec []int) Disk {
	return Disk{spec: spec, blocks: ExpandSpec(spec)}
}

func ExpandSpec(spec []int) []rune {
	ret := []rune{}
	id := 48
	for i := range spec {
		if i%2 != 0 {
			// free space
			for j := 0; j < spec[i]; j++ {
				ret = append(ret, '.')
			}
		} else {
			// Blocks
			for j := 0; j < spec[i]; j++ {
				ret = append(ret, rune(id))
			}
			id++
		}

	}
	return ret
}

func (d *Disk) Defrag() []rune {
	ret := DefragBlocks(d.blocks)
	d.blocks = ret
	return ret
}

func (d *Disk) Checksum() int {
	ret := 0
	for i := 0; i < len(d.blocks); i++ {
		if int(d.blocks[i]) != 46 {
			ret += i * (int(d.blocks[i]) - 48)
		}
	}
	return ret
}

func main() {
	fmt.Println("Hello.")
	lines, err := aocutil.GetIntMatrixFromFile(os.Args[1], "")
	if err != nil {
		fmt.Println("opening file: ", err)
		os.Exit(1)
	}

	d := NewDisk(lines[0])

	fmt.Println("Blocks: ", string(d.blocks))

	fmt.Println("Defragged: ", string(d.Defrag()))

	fmt.Println("Part 1: ", d.Checksum())

}

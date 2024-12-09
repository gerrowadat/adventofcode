package main

import (
	"fmt"
	"os"
	"slices"

	"github.com/gerrowadat/adventofcode/aocutil"
)

type File struct {
	id, start, size int
}
type Disk struct {
	spec   []int
	blocks []rune
	files  []File
}

func LastFilledBlock(b []rune) int {
	for i := len(b) - 1; i >= 0; i-- {
		if b[i] != 46 {
			return i
		}
	}
	return -1
}

func FirstFreeBlock(b []rune) int {
	for i := 0; i < len(b); i++ {
		if b[i] == 46 {
			return i
		}
	}
	return -1
}

func FirstFreeSpace(b []rune, l int) int {
	//fmt.Printf("Looking for %d in %s\n", l, string(b))
	for i := 0; i < len(b); i++ {
		if i+l > len(b) {
			break
		}
		if b[i] == 46 {
			found := true
			for j := 0; j < l; j++ {
				if b[i+j] != 46 {
					found = false
					break
				}
			}
			if found {
				return i
			}
		}
	}
	return -1
}

func NewDisk(spec []int) Disk {
	b := ExpandSpec(spec)
	return Disk{spec: spec, blocks: b, files: FindFiles(b)}
}

func FindFiles(b []rune) []File {
	ret := []File{}
	c := 0
	for c < len(b) {
		if b[c] == 46 {
			c++
		} else {
			f := File{id: int(b[c]), start: c}
			l := 0
			for c+l < len(b) && int(b[c+l]) == f.id {
				l++
			}
			f.size = l
			ret = append(ret, f)
			c += l
		}
	}
	return ret
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

func (d *Disk) DefragBlocks() []rune {
	ret := make([]rune, len(d.blocks))
	copy(ret, d.blocks)
	lf := LastFilledBlock(ret)
	ff := FirstFreeBlock(ret)
	for lf > ff {
		//fmt.Printf("Defragging Block %d[%v] into block %d[%v]\n", lf, ret[lf], ff, ret[ff])
		ret[ff] = ret[lf]
		ret[lf] = '.'
		lf = LastFilledBlock(ret)
		ff = FirstFreeBlock(ret)
		//fmt.Println(string(ret))
	}
	d.blocks = ret
	return ret
}

func (d *Disk) DefragFiles() []rune {
	ret := make([]rune, len(d.blocks))
	copy(ret, d.blocks)

	file_ids := []int{}
	for _, f := range d.files {
		if slices.Index(file_ids, f.id) == -1 {
			file_ids = append(file_ids, f.id)
		}
	}
	slices.Sort(file_ids)
	slices.Reverse(file_ids)

	for _, f := range file_ids {
		// Find a space for the file, and move it (or not)
		file := File{}
		for i := range d.files {
			if d.files[i].id == f {
				file = d.files[i]
				break
			}
		}
		space := FirstFreeSpace(ret, file.size)
		if space == -1 {
			// Skip if no space.
			continue
		}
		// files always shift lower
		if space > file.start {
			continue
		}
		// Swap the file to its new home.
		for i := 0; i < file.size; i++ {
			ret[space+i] = ret[file.start+i]
			ret[file.start+i] = '.'
		}
	}

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

	bd := NewDisk(lines[0])
	bd.DefragBlocks()
	fmt.Println("Part 1: ", bd.Checksum())

	fd := NewDisk(lines[0])
	fd.DefragFiles()
	fmt.Println("Part 2: ", fd.Checksum())
}

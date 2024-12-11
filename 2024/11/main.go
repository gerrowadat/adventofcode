package main

import (
	"fmt"
	"os"
	"strconv"

	"github.com/gerrowadat/adventofcode/aocutil"
)

type Node struct {
	data int
	next *Node
}

func NewNode(data int) Node {
	return Node{data: data, next: nil}
}

type Stones struct {
	head *Node
}

func NewStones() Stones {
	return Stones{head: nil}
}

func (s *Stones) InsertAtEnd(newn Node) {
	if s.head == nil {
		s.head = &newn
		return
	}

	n := s.head
	for n.next != nil {
		n = n.next
	}
	n.next = &newn
}

func (s *Stones) String() string {
	ret := ""
	if s.head != nil {
		ret += fmt.Sprintf("%d", s.head.data)
	}
	n := s.head.next

	for n != nil {
		ret += fmt.Sprintf(" -> %d", n.data)
		n = n.next
	}

	return ret
}

func ExpandStones(data int) Stones {
	ret := NewStones()
	if data == 0 {
		ret.InsertAtEnd(NewNode(1))
		return ret
	}
	data_str := fmt.Sprintf("%d", data)
	if len(data_str)%2 == 0 {
		s1, err := strconv.Atoi(data_str[0 : len(data_str)/2])
		if err != nil {
			fmt.Printf("Weird: %s\n", data_str)
			os.Exit(1)
		}
		s2, err := strconv.Atoi(data_str[len(data_str)/2:])
		if err != nil {
			fmt.Printf("Weird: %s\n", data_str)
			os.Exit(1)
		}
		ret.InsertAtEnd(NewNode(s1))
		ret.InsertAtEnd(NewNode(s2))
		return ret
	} else {
		ret.InsertAtEnd(NewNode(data * 2024))
		return ret
	}
}

func (s *Stones) Blink() {
	c := s.head

	for c != nil {
		if c.data == 0 {
			c.data = 1
			c = c.next
			continue
		}
		data_str := fmt.Sprintf("%d", c.data)
		if len(data_str)%2 != 0 {
			// odd number of digits
			c.data = c.data * 2024
		} else {
			// even number of digits
			s1, err := strconv.Atoi(data_str[0 : len(data_str)/2])
			if err != nil {
				fmt.Printf("Weird: %s\n", data_str)
				os.Exit(1)
			}
			s2, err := strconv.Atoi(data_str[len(data_str)/2:])
			if err != nil {
				fmt.Printf("Weird: %s\n", data_str)
				os.Exit(1)
			}
			c.data = s1
			old_next := c.next
			new_next := NewNode(s2)
			c.next = &new_next
			c.next.next = old_next
			c = &new_next
		}
		c = c.next
	}
}

func (s *Stones) Len() int {
	if s.head == nil {
		return 0
	}
	n := s.head
	ret := 0

	for n != nil {
		ret++
		n = n.next
	}
	return ret
}

func main() {
	fmt.Println("Hello.")
	lines, err := aocutil.GetIntMatrixFromFile(os.Args[1], " ")
	if err != nil {
		fmt.Println("opening file: ", err)
		os.Exit(1)
	}

	s := NewStones()

	for i := range lines[0] {
		s.InsertAtEnd(NewNode(lines[0][i]))
	}

	for range 25 {
		s.Blink()
		//fmt.Println(s.String())
	}
	fmt.Println("Part 1: ", s.Len())

}

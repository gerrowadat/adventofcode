package main

import (
	"fmt"
	"strconv"
	"strings"
)

type MapEntry struct {
	src, dest, range_len int
}

type AlmanacMap struct {
	entries []*MapEntry
}

func (m *AlmanacMap) get(i int) int {
	for _, e := range m.entries {
		//fmt.Printf(" + src %d dest %d range %d\n", e.src, e.dest, e.range_len)
		if e.src <= i && i <= e.src+e.range_len {
			//fmt.Printf(" -- %d falls between %d and %d :  %d -> %d\n", i, e.src, e.src+e.range_len, i, e.dest+e.range_len)
			return e.dest + (i - e.src)
		}
	}
	//fmt.Printf(" -- %d -> %d\n", i, i)
	return i
}

func (m *AlmanacMap) load_raw_entry(raw string) {
	fields := strings.Fields(raw)
	if len(fields) != 3 {
		fmt.Printf("Wrong number of fields in map entry: %s\n", raw)
		return
	}

	dest_start, err := strconv.Atoi(fields[0])
	if err != nil {
		fmt.Printf("Error getting dest_start from '%s'\n", fields[0])
		return
	}
	src_start, err := strconv.Atoi(fields[1])
	if err != nil {
		fmt.Printf("Error getting src_start from '%s'\n", fields[1])
		return
	}
	range_len, err := strconv.Atoi(fields[2])
	if err != nil {
		fmt.Printf("Error getting range_len from '%s'\n", fields[2])
		return
	}

	fmt.Printf(" --- src %d dest %d range %d\n", src_start, dest_start, range_len)
	m.entries = append(m.entries, &MapEntry{
		src: src_start, dest: dest_start, range_len: range_len})
}

func getSeedList(raw string) []int {
	strlist := strings.Fields(strings.Split(raw, ":")[1])
	ret := []int{}
	for _, i := range strlist {
		j, err := strconv.Atoi(i)
		if err != nil {
			fmt.Printf("Funny-looking seed number '%s'\n", i)
		}
		ret = append(ret, j)
	}
	return ret
}

func getMap(raw []string, mapname *string) *AlmanacMap {
	ret := &AlmanacMap{}

	want := fmt.Sprintf("%s map:", *mapname)

	scanning := false
	for i, l := range raw {
		if l == want {
			fmt.Printf("Found %s, scanning...\n", *mapname)
			scanning = true
			continue
		}
		if scanning == true {
			if l == "" || i+1 == len(raw) {
				// Scan done, return what we have.
				return ret
			}
			// Otherwise load the next line into the AlmanacMap
			fmt.Printf(" - %s\n", l)
			ret.load_raw_entry(l)
		}
	}

	// should only get here if the desired map is missing.
	fmt.Printf("Desired map missing: %s\n", *mapname)
	return nil
}

func main() {
	lines := getFileLines("input.txt")

	seeds := getSeedList(lines[0])

	mapnames := []string{
		"seed-to-soil",
		"soil-to-fertilizer",
		"fertilizer-to-water",
		"water-to-light",
		"light-to-temperature",
		"temperature-to-humidity",
		"humidity-to-location",
	}

	maps := make(map[string]*AlmanacMap, len(mapnames))

	for _, m := range mapnames {
		maps[m] = getMap(lines, &m)
	}

	fmt.Println("")

	min_loc := 0
	for _, s := range seeds {
		val := s
		for _, m := range mapnames {
			old_val := val
			val = maps[m].get(val)
			fmt.Printf(" == %d -> %s -> %d\n", old_val, m, val)

		}
		if min_loc == 0 || val < min_loc {
			min_loc = val
		}
		fmt.Printf("Seed %d goes in location %d\n", s, val)
	}
	fmt.Printf("Closest Location: %d\n", min_loc)
}

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

type SeedRange struct {
	start, size int
}

func (m *AlmanacMap) get(i int) int {
	for _, e := range m.entries {
		if e.src <= i && i <= e.src+e.range_len {
			return e.dest + (i - e.src)
		}
	}
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

	m.entries = append(m.entries, &MapEntry{
		src: src_start, dest: dest_start, range_len: range_len})
}

func getSimpleSeedList(raw string) []int {
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

func getRangedSeedList(raw string) []*SeedRange {
	strlist := strings.Fields(strings.Split(raw, ":")[1])
	ret := []*SeedRange{}
	nums := []int{}
	for _, i := range strlist {
		j, err := strconv.Atoi(i)
		if err != nil {
			fmt.Printf("Funny-looking seed number '%s'\n", i)
		}
		nums = append(nums, j)
	}
	for i := 0; i < len(nums); i += 2 {
		ret = append(ret, &SeedRange{start: nums[i], size: nums[i+1]})
	}
	return ret
}

func getMap(raw []string, mapname *string) *AlmanacMap {
	ret := &AlmanacMap{}

	want := fmt.Sprintf("%s map:", *mapname)

	scanning := false
	for i, l := range raw {
		if l == want {
			scanning = true
			continue
		}
		if scanning == true {
			if l == "" || i+1 == len(raw) {
				// Scan done, return what we have.
				return ret
			}
			// Otherwise load the next line into the AlmanacMap
			ret.load_raw_entry(l)
		}
	}

	// should only get here if the desired map is missing.
	fmt.Printf("Desired map missing: %s\n", *mapname)
	return nil
}

func getClosestLocationList(seeds []int, maps map[string]*AlmanacMap, mapnames []string) int {
	ret := 0
	for _, s := range seeds {
		val := s
		for _, m := range mapnames {
			//old_val := val
			val = maps[m].get(val)
			//fmt.Printf(" == %d -> %s -> %d\n", old_val, m, val)

		}
		if ret == 0 || val < ret {
			ret = val
		}
	}
	return ret
}

func getClosestLocationRange(seed_ranges []*SeedRange, maps map[string]*AlmanacMap, mapnames []string) int {
	ret := 0
	for _, s := range seed_ranges {
		fmt.Printf("Processing range %d (%d entries)...", s.start, s.size)
		count := 0
		for i := s.start; i <= s.start+s.size; i++ {
			val := i
			for _, m := range mapnames {
				//old_val := val
				val = maps[m].get(val)
				//fmt.Printf(" == %d -> %s -> %d\n", old_val, m, val)

			}
			if ret == 0 || val < ret {
				ret = val
			}
			count++
			if count > 1000000 {
				fmt.Printf(".")
				count = 0
			}
		}
	}
	return ret
}

func main() {
	lines := getFileLines("input.txt")

	seeds := getSimpleSeedList(lines[0])
	range_seeds := getRangedSeedList(lines[0])
	fmt.Printf("Ranged seed list includes %d seeds.\n", len(range_seeds))

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

	fmt.Printf("Part 1: %d\n", getClosestLocationList(seeds, maps, mapnames))
	fmt.Printf("Part 2: %d\n", getClosestLocationRange(range_seeds, maps, mapnames))
}

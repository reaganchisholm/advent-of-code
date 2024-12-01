package main

import (
	"log"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	// exampleData := `3   4
	// 4   3
	// 2   5
	// 1   3
	// 3   9
	// 3   3`
	data, _ := os.ReadFile("input.txt")

	var total int
	var simTotal int
	l, r := buildList(string(data))

	for i := 0; i < len(l); i++ {
		numL, _ := strconv.Atoi(l[i])
		numR, _ := strconv.Atoi(r[i])

		// Part 1
		total = total + diff(numL, numR)

		// Part 2
		occNum := count(l[i], r)
		simTotal = simTotal + (numL * occNum)
	}

	log.Printf("--------- Part 1: %d", total)
	log.Printf("--------- Part 2: %d", simTotal)
}

func buildList(rawString string) ([]string, []string) {
	lines := strings.Split(rawString, "\n")
	var leftList []string
	var rightList []string

	for i := 0; i < len(lines); i++ {
		splitLine := strings.Split(lines[i], "   ")

		leftList = append(leftList, strings.TrimSpace(splitLine[0]))
		rightList = append(rightList, strings.TrimSpace(splitLine[1]))
	}

	// Sort em
	sort.Sort(sort.StringSlice(leftList))
	sort.Sort(sort.StringSlice(rightList))

	return leftList, rightList
}

func diff(a, b int) int {
	if a < b {
		return b - a
	}
	return a - b
}

func count(x string, slice []string) int {
	count := 0

	for _, numStr := range slice {
		if numStr == x {
			count++
		}
	}

	return count
}

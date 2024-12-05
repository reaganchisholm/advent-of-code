package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func main() {
	part1()
	part2()
}

func part1() {
	// exampleData := `xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))`
	dataBytes, err := os.ReadFile("input.txt")
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}
	data := string(dataBytes)

	r, _ := regexp.Compile(`mul\(\d+,\d+\)`)
	muls := r.FindAllString(data, -1)
	var total int

	for i := 0; i < len(muls); i++ {
		result := multiply(muls[i])
		total = total + result
	}

	println("Part 1 --------- ", total)
}

func part2() {
	// exampleData := `xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))`
	dataBytes, err := os.ReadFile("input.txt")
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}
	data := string(dataBytes)

	r, _ := regexp.Compile(`(mul\(\d+,\d+\))|(don't\(\))|do\(\)`)
	muls := r.FindAllString(data, -1)
	var total int
	var status int

	for i := 0; i < len(muls); i++ {
		// log.Print("Testing: ", muls[i])
		if strings.Contains(muls[i], "don't") {
			status = -1
			continue
		} else if strings.Contains(muls[i], "do") {
			status = 1
			continue
		}

		if status == 0 || status == 1 {
			// log.Print("Processing: ", muls[i])
			result := multiply(muls[i])
			total = total + result
			status = 0
		} else {
			// println("Skipping: ", muls[i])
		}
	}

	println("Part 2 --------- ", total)
}

func multiply(str string) int {
	stripped := strings.ReplaceAll(str, "mul(", "")
	stripped = strings.ReplaceAll(stripped, ")", "")
	chars := strings.Split(stripped, ",")
	a, _ := strconv.Atoi(chars[0])
	b, _ := strconv.Atoi(chars[1])
	return a * b
}

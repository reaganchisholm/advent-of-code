package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	part1()
	part2()
}

func part1() {
	// 	data := `47|53
	// 97|13
	// 97|61
	// 97|47
	// 75|29
	// 61|13
	// 75|53
	// 29|13
	// 97|29
	// 53|29
	// 61|53
	// 97|53
	// 61|29
	// 47|13
	// 75|47
	// 97|75
	// 47|61
	// 75|61
	// 47|29
	// 75|13
	// 53|13

	// 75,47,61,53,29
	// 97,61,53,29,13
	// 75,29,13
	// 75,97,47,61,53
	// 61,13,29
	// 97,13,75,29,47`

	dataBytes, err := os.ReadFile("input.txt")
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	data := string(dataBytes)
	instr, data := strings.Split(data, "\n\n")[0], strings.Split(data, "\n\n")[1]
	var total int

	// Set up the instructions
	instructions := make(map[int][]int)
	for _, line := range strings.Split(instr, "\n") {
		strOne, strTwo := strings.Split(line, "|")[0], strings.Split(line, "|")[1]
		numOne, _ := strconv.Atoi(strOne)
		numTwo, _ := strconv.Atoi(strTwo)

		instructions[numOne] = append(instructions[numOne], numTwo)
	}

	// Set up the data
	dataArr := make([][]int, 0)
	for _, line := range strings.Split(data, "\n") {
		nums := strings.Split(line, ",")
		numArr := make([]int, 0)
		for _, num := range nums {
			numInt, _ := strconv.Atoi(num)
			numArr = append(numArr, numInt)
		}
		dataArr = append(dataArr, numArr)
	}

	// Now we test the data
	for _, data := range dataArr {
		if isValid(instructions, data) {
			middleNum := data[len(data)/2]
			total = total + middleNum
		}
	}

	println("Part 1 --------- ", total)
}

func part2() {
	data := `47|53
	97|13
	97|61
	97|47
	75|29
	61|13
	75|53
	29|13
	97|29
	53|29
	61|53
	97|53
	61|29
	47|13
	75|47
	97|75
	47|61
	75|61
	47|29
	75|13
	53|13

	// 75,47,61,53,29
	// 97,61,53,29,13
	// 75,29,13
	// 75,97,47,61,53
	// 61,13,29
	// 97,13,75,29,47`

	// dataBytes, err := os.ReadFile("input.txt")
	// if err != nil {
	// 	fmt.Println("Error reading file:", err)
	// 	return
	// }

	// data := string(dataBytes)
	instr, data := strings.Split(data, "\n\n")[0], strings.Split(data, "\n\n")[1]
	var total int

	// Set up the instructions
	instructions := make(map[int][]int)
	for _, line := range strings.Split(instr, "\n") {
		strOne, strTwo := strings.Split(line, "|")[0], strings.Split(line, "|")[1]
		numOne, _ := strconv.Atoi(strOne)
		numTwo, _ := strconv.Atoi(strTwo)

		instructions[numOne] = append(instructions[numOne], numTwo)
	}

	// Set up the data
	dataArr := make([][]int, 0)
	for _, line := range strings.Split(data, "\n") {
		nums := strings.Split(line, ",")
		numArr := make([]int, 0)
		for _, num := range nums {
			numInt, _ := strconv.Atoi(num)
			numArr = append(numArr, numInt)
		}
		dataArr = append(dataArr, numArr)
	}

	// Now we test the data
	for _, data := range dataArr {
		if isValid(instructions, data) == false {
			fixedLine := fixLine(instructions, data)
			middleNum := fixedLine[len(fixedLine)/2]
			total = total + middleNum
		}
	}

	println("Part 2 --------- ", total)
}

func isValid(instructions map[int][]int, data []int) bool {
	isValid := true

	for i := 0; i < len(data)-1; i++ {
		if Contains(instructions[data[i]], data[i+1]) == false {
			isValid = false
			break
		}
	}

	return isValid
}

func fixLine(instructions map[int][]int, data []int) []int {
	fixedLine := make([]int, 0)
	firstNum := data[0]
	fixedLine = append(fixedLine, firstNum)

	return fixedLine
}

func Contains[T comparable](s []T, e T) bool {
	for _, v := range s {
		if v == e {
			return true
		}
	}
	return false
}

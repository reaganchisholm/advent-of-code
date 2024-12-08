package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	part1()
	part2()
}

func part1() {
	// 	data := `MMMSXXMASM
	// MSAMXMSMSA
	// AMXSXMAAMM
	// MSAMASMSMX
	// XMASAMXAMM
	// XXAMMXXAMA
	// SMSMSASXSS
	// SAXAMASAAA
	// MAMMMXMMMM
	// MXMXAXMASX`
	dataBytes, err := os.ReadFile("input.txt")
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	data := string(dataBytes)
	lines := strings.Fields(strings.TrimSpace(data))

	grid := make([][]rune, len(lines))
	for i, line := range lines {
		grid[i] = []rune(line)
	}

	total := 0
	for h, row := range grid {
		for j, cell := range row {
			letter := string(cell)
			if letter == "X" {
				total = total + check(h, j, grid)
			}
		}
	}

	println("Part 1 --------- ", total)
}

func part2() {
	// println("Part 2 --------- ", 0)
}

func check(x int, y int, grid [][]rune) int {
	var amountFound int
	word := "XMAS"

	var left []rune
	left = append(left, grid[x][y])
	for i := 1; i < 4; i++ {
		if y-i >= 0 {
			left = append(left, grid[x][y-i])
		} else {
			break // Stop if index goes out of bounds
		}
	}

	var right []rune
	right = append(right, grid[x][y])
	for i := 1; i < 4; i++ {
		if y+i < len(grid[x]) {
			right = append(right, grid[x][y+i])
		} else {
			break // Stop if index goes out of bounds
		}
	}

	var up []rune
	up = append(up, grid[x][y])
	for i := 1; i < 4; i++ {
		if x-i >= 0 {
			up = append(up, grid[x-i][y])
		} else {
			break // Stop if index goes out of bounds
		}
	}

	var down []rune
	down = append(down, grid[x][y])
	for i := 1; i < 4; i++ {
		if x+i < len(grid) {
			down = append(down, grid[x+i][y])
		} else {
			break // Stop if index goes out of bounds
		}
	}

	var diagUpLeft []rune
	diagUpLeft = append(diagUpLeft, grid[x][y])
	for i := 1; i < 4; i++ {
		if x-i >= 0 && y-i >= 0 {
			diagUpLeft = append(diagUpLeft, grid[x-i][y-i])
		} else {
			break // Stop if index goes out of bounds
		}
	}

	var diagUpRight []rune
	diagUpRight = append(diagUpRight, grid[x][y])
	for i := 1; i < 4; i++ {
		if x-i >= 0 && y+i < len(grid[x]) {
			diagUpRight = append(diagUpRight, grid[x-i][y+i])
		} else {
			break // Stop if index goes out of bounds
		}
	}

	var diagDownLeft []rune
	diagDownLeft = append(diagDownLeft, grid[x][y])
	for i := 1; i < 4; i++ {
		if x+i < len(grid) && y-i >= 0 {
			diagDownLeft = append(diagDownLeft, grid[x+i][y-i])
		} else {
			break // Stop if index goes out of bounds
		}
	}

	var diagDownRight []rune
	diagDownRight = append(diagDownRight, grid[x][y])
	for i := 1; i < 4; i++ {
		if x+i < len(grid) && y+i < len(grid[x]) {
			diagDownRight = append(diagDownRight, grid[x+i][y+i])
		} else {
			break // Stop if index goes out of bounds
		}
	}

	// -----------------------------------------------------

	if string(left) == word {
		amountFound++
	}

	if string(right) == word {
		amountFound++
	}

	if string(up) == word {
		amountFound++
	}

	if string(down) == word {
		amountFound++
	}

	if string(diagUpLeft) == word {
		amountFound++
	}

	if string(diagUpRight) == word {
		amountFound++
	}

	if string(diagDownLeft) == word {
		amountFound++
	}

	if string(diagDownRight) == word {
		amountFound++
	}

	return amountFound
}

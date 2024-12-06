package main

import (
	"log"
	"strings"
)

func main() {
	part1()
	part2()
}

func part1() {
	data := `MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX`

	// target := "XMAS"
	lines := strings.Split(data, "\n")

	for i := 0; i < len(lines); i++ {
		chars := strings.Split(lines[i], "")
		for j := 0; j < len(chars); j++ {
			c := chars[j]
			log.Print(c)
		}
	}

	println("Part 1 --------- ", 0)
}

func part2() {
	println("Part 2 --------- ", 0)
}

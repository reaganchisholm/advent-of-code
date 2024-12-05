package main

import (
	"os"
	"strconv"
	"strings"
)

func main() {
	part1()
	part2()
}

func part1() {
	// 	exampleData := `7 6 4 2 1
	// 1 2 7 8 9
	// 9 7 6 2 1
	// 1 3 2 4 5
	// 8 6 4 4 1
	// 1 3 6 7 9`
	data, _ := os.ReadFile("input.txt")

	lines := strings.Split(string(data), "\n")
	safeCount := 0

	for i := 0; i < len(lines); i++ {
		line := strings.TrimSpace(lines[i])
		result := test(line)

		if result > 0 {
			safeCount++
		}
	}

	println("Part 1 --------- ", safeCount)
}

func part2() {
	// 	exampleData := `7 6 4 2 1
	// 1 2 7 8 9
	// 9 7 6 2 1
	// 1 3 2 4 5
	// 8 6 4 4 1
	// 1 3 6 7 9`
	data, _ := os.ReadFile("input.txt")

	lines := strings.Split(string(data), "\n")
	safeCount := 0

	for i := 0; i < len(lines); i++ {
		// log.Print("- Testing Line: ", lines[i])
		multiFails := false
		tmpSafeCount := test(lines[i])
		if tmpSafeCount == -1 {
			chars := strings.Split(lines[i], " ")
			for j := 0; j < len(chars); j++ {
				copyOfChars := make([]string, len(chars))
				copy(copyOfChars, chars)
				lineMinus := strings.Join(remove(copyOfChars, j), " ")
				// log.Print("-- Testing Line: ", lineMinus)
				tmpSafeCount = tmpSafeCount + test(lineMinus)
			}

			if tmpSafeCount == (len(chars)+1)*-1 {
				multiFails = true
			}
		}

		if !multiFails {
			safeCount++
		} else {
			// log.Print("! Line Failed: ", lines[i])
		}
	}

	println("Part 2 --------- ", safeCount)
}

func test(str string) int {
	line := strings.TrimSpace(str)
	chars := strings.Split(line, " ")
	direction := 0
	var safe bool

	for j := 0; j < len(chars); j++ {
		char := chars[j]
		var nChar string
		safe = true

		if j < len(chars)-1 {
			nChar = chars[j+1]
		}

		if nChar != "" {
			c1, _ := strconv.Atoi(char)
			c2, _ := strconv.Atoi(nChar)

			if c1 < c2 {
				if direction == -1 {
					safe = false
					break
				}
				direction = 1
			} else if c1 > c2 {
				if direction == 1 {
					safe = false
					break
				}
				direction = -1
			} else {
				safe = false
				break
			}

			d := diff(c1, c2)
			if d < 1 || d > 3 {
				safe = false
				break
			}
		}
	}

	if safe {
		return 1
	} else {
		return -1
	}
}

func remove(slice []string, s int) []string {
	return append(slice[:s], slice[s+1:]...)
}

func diff(a, b int) int {
	if a > b {
		return a - b
	}
	return b - a
}

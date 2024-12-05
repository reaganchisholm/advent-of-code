package main

import (
	"os"
	"strconv"
	"strings"
)

func diff(a, b int) int {
	if a > b {
		return a - b
	}
	return b - a
}

func main() {
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
						// println("direction change")
						break
					}
					direction = 1
				} else if c1 > c2 {
					if direction == 1 {
						safe = false
						// println("direction change")
						break
					}
					direction = -1
				} else {
					// Same number
					safe = false
					// println("same number")
					break
				}

				d := diff(c1, c2)
				if d < 1 || d > 3 {
					// println("diff too much: %d", d)
					safe = false
					break
				}
			}
		}

		// println(line, safe)

		if safe {
			safeCount++
		}
	}

	println("Part 1 --------- ", safeCount)
}

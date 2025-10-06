package main

import (
	"bufio"
	"fmt"
	"os"
)

var io = bufio.NewReadWriter(
	bufio.NewReader(os.Stdin),
	bufio.NewWriter(os.Stdout),
)

func main() {
	defer io.Flush()

	var n int
	fmt.Fscan(io, &n)

	scores := make([]int, n)
	max := 0
	for i := 0; i < n; i++ {
		fmt.Fscan(io, &scores[i])
		if max < scores[i] {
			max = scores[i]
		}
	}

	sum := 0.0
	for _, score := range scores {
		sum += float64(score) / float64(max) * 100.0
	}

	result := sum / float64(n)
	fmt.Fprintln(io, result)
}

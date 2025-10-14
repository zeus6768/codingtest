package main

import (
	"bufio"
	"fmt"
	"os"
)

var MIN = -1_000_000
var MAX = 1_000_000

var io = bufio.NewReadWriter(
	bufio.NewReader(os.Stdin),
	bufio.NewWriter(os.Stdout),
)

func main() {
	defer io.Flush()

	var N int
	fmt.Fscan(io, &N)

	nums := make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Fscan(io, &nums[i])
	}

	min := MAX
	max := MIN
	for _, num := range nums {
		if num < min {
			min = num
		}
		if num > max {
			max = num
		}
	}

	fmt.Fprintf(io, "%d %d\n", min, max)
}

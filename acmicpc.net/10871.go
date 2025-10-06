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

	var N, X int
	fmt.Fscanf(io, "%d %d\n", &N, &X)

	nums := make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Fscan(io, &nums[i])
	}

	for _, num := range nums {
		if num < X {
			fmt.Fprintf(io, "%d ", num)
		}
	}
}

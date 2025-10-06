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

	nums := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(io, &nums[i])
	}

	var v int
	fmt.Fscan(io, &v)

	var count int
	for _, num := range nums {
		if num == v {
			count++
		}
	}

	fmt.Fprintln(io, count)
}

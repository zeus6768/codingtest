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

	var N, M int
	fmt.Fscanln(io, &N, &M)

	var basket []int
	basket = make([]int, N)

	var i, j, k int
	for m := 0; m < M; m++ {
		fmt.Fscanln(io, &i, &j, &k)
		for n := i - 1; n < j; n++ {
			basket[n] = k
		}
	}

	for m := 0; m < N; m++ {
		fmt.Fprint(io, basket[m])
		if m < N-1 {
			fmt.Fprint(io, " ")
		}
	}
	fmt.Fprintln(io)
}

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

	basket := make([]int, N)
	for i := range N {
		basket[i] = i + 1
	}

	for range M {
		var i, j int
		fmt.Fscanln(io, &i, &j)
		i -= 1
		j -= 1
		for i < j {
			basket[i], basket[j] = basket[j], basket[i]
			i++
			j--
		}
	}

	for i, num := range basket {
		fmt.Fprint(io, num)
		if i < N-1 {
			fmt.Fprint(io, " ")
		}
	}
	fmt.Fprintln(io)
}

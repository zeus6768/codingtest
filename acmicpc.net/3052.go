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

	N := 10
	num := 0
	remainders := make([]int, N)
	for i := range N {
		fmt.Fscan(io, &num)
		remainders[i] = num % 42
	}

	uniqueNumSet := make(map[int]struct{})
	for _, remainder := range remainders {
		uniqueNumSet[remainder] = struct{}{}
	}

	fmt.Fprintln(io, len(uniqueNumSet))
}

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

var SIZE = 9

func main() {
	defer io.Flush()

	var num, order int
	max := 0
	for i := 1; i <= SIZE; i++ {
		fmt.Fscan(io, &num)
		if max < num {
			max = num
			order = i
		}
	}
	fmt.Fprintf(io, "%d\n%d\n", max, order)
}

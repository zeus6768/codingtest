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
	var s string
	fmt.Fscan(io, &s)

	indexes := make([]int, 26)
	for i := range 26 {
		indexes[i] = -1
	}

	for i, c := range s {
		index := int(c - 'a')
		if indexes[index] == -1 {
			indexes[index] = i
		}
	}

	for _, index := range indexes {
		fmt.Fprintf(io, "%d ", index)
	}

	io.Flush()
}

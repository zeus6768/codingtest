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

	var T int
	fmt.Fscanln(io, &T)

	var s string
	for range T {
		fmt.Fscanln(io, &s)
		fmt.Fprintf(io, "%c%c\n", s[0], s[len(s)-1])
	}
}

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

	var S string
	fmt.Fscanln(io, &S)

	var i int
	fmt.Fscanln(io, &i)

	fmt.Fprintf(io, "%c\n", S[i-1])
}

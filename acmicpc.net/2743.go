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

	var word string
	fmt.Fscan(io, &word)

	fmt.Fprintln(io, len(word))
}

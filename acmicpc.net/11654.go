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
	c, _, _ := io.ReadRune()
	fmt.Fprintln(io, c)
	io.Flush()
}

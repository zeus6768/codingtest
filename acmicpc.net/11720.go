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
	var n int
	fmt.Fscan(io, &n)

	var numbers []byte
	fmt.Fscan(io, &numbers)

	var sum int
	for _, number := range numbers {
		sum += int(number - '0')
	}

	fmt.Fprintln(io, sum)

	io.Flush()
}

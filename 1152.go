package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

var io = bufio.NewReadWriter(
	bufio.NewReader(os.Stdin),
	bufio.NewWriter(os.Stdout),
)

func main() {
	input, _ := io.ReadString('\n')
	input = strings.TrimSpace(input)
	words := strings.Fields(input)
	fmt.Fprintln(io, len(words))
	io.Flush()
}

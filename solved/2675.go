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
	var t int
	fmt.Fscan(io, &t)

	var r int
	var s string
	for range t {
		fmt.Fscan(io, &r, &s)
		var newString []rune
		for _, c := range s {
			for range r {
				newString = append(newString, c)
			}
		}
		fmt.Fprintln(io, string(newString))
	}

	io.Flush()
}

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

var STUDENT_TOTAL_COUNT = 30
var SUBMITTER_COUNT = 28

func main() {
	defer io.Flush()

	submitCheckList := make([]bool, STUDENT_TOTAL_COUNT+1)
	var studentNumber int
	for i := 0; i < SUBMITTER_COUNT; i++ {
		fmt.Fscanln(io, &studentNumber)
		submitCheckList[studentNumber] = true
	}

	for i := 1; i <= STUDENT_TOTAL_COUNT; i++ {
		if !submitCheckList[i] {
			fmt.Fprintln(io, i)
		}
	}
}

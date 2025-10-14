package main

import (
	"fmt"
)

func reverse(n int) int {
	return (n%10)*100 + ((n/10)%10)*10 + n/100
}

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	a = reverse(a)
	b = reverse(b)
	if a > b {
		fmt.Println(a)
		return
	}
	fmt.Println(b)
}

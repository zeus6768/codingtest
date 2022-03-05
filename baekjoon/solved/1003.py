from sys import stdin
input = stdin.readline

def fibo(n):
	memory = {}
	for i in range(n+1):
		if i == 0:
			memory[0] = (1, 0)
		elif i == 1:
			memory[1] = (0, 1)
		else:
			memory[i] = (memory[i-1][0] + memory[i-2][0], memory[i-1][1] + memory[i-2][1])
	return memory[n]

def main():
	t = int(input())
	for _ in range(t):
		n = int(input())
		result = fibo(n)
		print(f"{result[0]} {result[1]}")

main()
def solve():

	n = int(input())

	f = [0] * (n+1)
	f[1], f[2] = 1, 1

	def fibonacci(n):
		for i in range(3, n+1):
			answer[1] += 1
			f[i] = f[i-1] + f[i-2]
		return f[n]
	
	answer = [0, 0]
	answer[0] = fibonacci(n)

	print(*answer)


solve()
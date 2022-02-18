def prime(m, n):
	is_prime = [True] * (n+1)
	for i in range(2, int(n**0.5)+1):
		if is_prime[i] == True:
			for j in range(i+i, n+1, i):
				is_prime[j] = False
	return sum(is_prime[m+1: n+1])

def solution():
	answer = []
	while True:
		n = int(input())
		if n:
			answer.append(prime(n, n*2))
		else:
			break
	[print(a) for a in answer]

solution()
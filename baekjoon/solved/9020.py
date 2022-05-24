import sys
input = sys.stdin.readline

def solution():

	def prime(n):
		is_prime = [True] * (n+1)
		for i in range(2, int(n**0.5)+1):
			if is_prime[i]:
				for j in range(i+i, n+1, i):
					is_prime[j] = False
		return [i for i in range(2, n+1) if is_prime[i]]

	for _ in range(int(input())):
		n = int(input())
		primes = prime(n)
		l, r = 0, len(primes)-1
		while l <= r:
			out = primes[l] + primes[r]
			if out < n:
				l += 1
			else:
				if out == n:
					result = [primes[l], primes[r]]
				r -= 1
		print(*result)

solution()

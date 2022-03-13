from sys import stdin
input = stdin.readline

def primes(n):
	is_prime = [True] * (n+1)
	for i in range(2, int(n**0.5)+1):
		if is_prime[i] == True:
			for j in range(i+i, n+1, i):
				is_prime[j] = False
	return [num for num in range(2, n) if is_prime[num]]

def solution(n):
	half = n // 2
	prime = primes(n)
	if half in prime:
		return [half, half]
	else:
		length = len(prime)
		for i in range(length//2, -1, -1):
			for j in range(length//2, length):
				if prime[i] + prime[j] == n:
						answer = (prime[i], prime[j])
						return answer

def main():
	t = int(input())
	numbers = sorted([int(input()) for _ in range(t)])
	[print(*solution(n)) for n in numbers]

main()
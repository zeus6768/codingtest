import sys

def input():
	return sys.stdin.readline()

def solve(N):
	answer = 0
	for prime in primes:
		if prime > N//2:
			break
		if N-prime in prime_set:
			answer += 1
	print(answer)

def get_primes(N):
	is_prime = [True] * (N+1)
	for i in range(2, int(N**0.5)+1):
		if is_prime[i]:
			for j in range(i+i, N+1, i):
				is_prime[j] = False
	return tuple(i for i in range(2, N+1) if is_prime[i])

if __name__ == "__main__":
	
	primes = get_primes(10**6)
	prime_set = set(primes)
	
	T = int(input())
	for _ in range(T):
		N = int(input())
		solve(N)
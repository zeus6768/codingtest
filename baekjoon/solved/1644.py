def primes(n):
	if n < 2:
		return [0]
	is_prime = [True] * (n+1)
	for i in range(2, n+1):
		if is_prime[i]:
			for j in range(i+i, n+1, i):
				is_prime[j] = False
	return [k for k in range(2, n+1) if is_prime[k]]

def solve():
	n = int(input())

	prime = primes(n)
	csum = [0]
	[csum.append(csum[i] + prime[i]) for i in range(len(prime))]
	
	answer = 0
	l, r = 0, 1

	while r <= len(prime):
		num = csum[r] - csum[l]
		if num == n:
			answer += 1
			l += 1
		elif num < n:
			r += 1
		else:
			l += 1
	
	print(answer)


solve()

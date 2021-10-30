import sys 

n = int(sys.stdin.readline().rstrip())

def factorization(num):
	prime = 2
	while num != 1:
		if (num % prime == 0):
			print(prime)
			num //= prime
		else:
			prime += 1

factorization(n)


# f(A) = A의 모든 약수의 합
# g(x) = sigma f(k)

def prime(n):
	is_prime = [1] * (n+1)
	for i in range(2, int(n**0.5)+1):
		if is_prime[i] == 1:
			for j in range(i+i, n+1, i):
				is_prime[j] = i
	return is_prime

N = int(input())
dp = {1: 1}
is_prime = prime(N)

def f(A) :
	if A in dp :
		return dp[A]
	else :
		if is_prime[A] == 1 :
			dp[A] = A+1
			return dp[A]
		else :
			i = is_prime[A]
			a = i
			while A % a == 0 :
				a *= i
			a //= i
			if (A // a) > 1 :
				dp[A] = f(a) * f(A//a)
			else :
				dp[A] = f(A//i) + A
			return dp[A]

def g(N) :
	return sum([f(i) for i in range(1, N+1)])

print(g(N))

# 12 = 3 * 2^2

# 0 1 3 = f(3) = 4
# 1 * (1 + 3)
# 2 * (1 + 3)
# 4 * (1 + 3)

# ==> (1+2+4) * (1+3) = f(4)*f(3)
# f(4) = 7

# 0 1 2 4 8

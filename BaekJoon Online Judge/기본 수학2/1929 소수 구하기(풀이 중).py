# 에라토스테네스의 체
m, n = map(int, input().split())
def solution(m, n):
	is_prime = [True] * (n+1)
	for i in range(2, int(n**0.5)+1):
		if is_prime[i] == True:
			for j in range(i+i, n+1, i):
				is_prime[j] = False
	[print(i) for i in range(m, n+1) if is_prime[i] == True]
solution(m, n)
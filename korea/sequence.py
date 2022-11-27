def solve():
	N = int(input())
	
	if N <= 2:
		answer = 3**N
	elif N == 3:
		answer = 26
	else:
		answer = 3 ** N - (2**(2*(N-3))+1) % 1_000_000_007

	print(answer)

solve()
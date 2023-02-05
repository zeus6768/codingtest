def solve():
    
	N = int(input())
	scores = list(map(int, input().split()))
	k = int(input())

	n = 2

	while n != N * 2 :
		tmp = []
		for i in range(N//n):
			tmp.extend(sorted(scores[i*n:i*n+n]))
		scores = tmp
		if N //n == k:
			print(*scores)
			return
		n *= 2

solve()
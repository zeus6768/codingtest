def solve():
	_, k = map(int, input().split())
	scores = sorted(map(int, input().split()), reverse=True)
	print(scores[k-1])

solve()
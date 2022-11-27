def solve() -> None:
	m = int(input())
	aliquots = sorted(map(int, input().split()))

	if m == 1:
		print(aliquots[0]**2)
	else:
		print(aliquots[0]*aliquots[-1])

solve()
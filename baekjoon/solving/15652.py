def solve():
	n, m = map(int, input().split())
	seq = []

	def go(idx):
		if len(seq) == m:
			print(*seq)
			return

		for i in range(idx, n+1):
			seq.append(i)
			go(i)
			seq.pop()

	go(1)

solve()
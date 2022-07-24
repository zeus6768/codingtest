def solve():

	n, m = map(int, input().split())
	seq = []

	def go():
		if len(seq) == m:
			print(*seq)
			return

		for i in range(1, n+1):
			seq.append(i)
			go()
			seq.pop()

	go()

solve()
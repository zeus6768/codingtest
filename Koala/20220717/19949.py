def solve():
	yj = list(map(int, input().split()))

	count = [0]
	seq = []
	
	def search(depth, score):

		if depth == 10:
			if score >= 5:
				count[0] += 1
			return
		
		for i in range(1, 6):
			if not (depth > 1 and seq[-1]==seq[-2]==i):
				seq.append(i)
				search(depth+1, score+(yj[depth]==i))
				seq.pop()

	search(0, 0)
	print(*count)

solve()
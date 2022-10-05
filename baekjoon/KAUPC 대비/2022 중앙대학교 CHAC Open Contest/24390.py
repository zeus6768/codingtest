def solve():
	M, S = map(int, input().split(':'))
	time = M*60 + S

	buttons = (10, 60, 600, 30)

	times = []

	q = [(0, 1)]
	while q:
		s, c = q.pop(0)
		times.append(s)
		for i in range(4):
			ns = s + buttons[i]
			if ns not in times:
				times.append(ns)
				q.append((ns, c+1))
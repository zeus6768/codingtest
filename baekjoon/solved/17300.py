def solve():
	
	L = int(input())
	A = list(map(int, input().split()))

	answer = "YES"

	if len(A) != len(set(A)):
		answer = "NO"
		print(answer)
		return

	impossible = [
		{},
		{3: 2, 7: 4, 9: 5},
		{8: 5},
		{1: 2, 7: 5, 9: 6},
		{6: 5},
		{},
		{4: 5},
		{1: 4, 3: 5, 9: 8},
		{2: 5},
		{1: 5, 3: 6, 7: 8}
	]

	visited = [False] * 10

	for i in range(L-1):
		now, next = A[i], A[i+1]
		visited[now] = True
		if next in impossible[now] and not visited[impossible[now][next]]:
			answer = "NO"
			break
		
	print(answer)

solve()

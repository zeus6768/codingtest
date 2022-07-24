def solve():
	n = int(input())
	visited = [0]*n
	answer = [0]

	def possible(q):
		for i in range(q):
			if visited[q] == visited[i] or abs(visited[q]-visited[i]) == abs(q-i):
				return False
		return True

	def queen(k):
		if k == n:
			answer[0] += 1
			return
		for i in range(n):
			visited[k] = i
			if possible(k):
				queen(k+1)

	queen(0)
	print(*answer)

solve()
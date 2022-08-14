from collections import deque

def solve():
	n, _ = map(int, input().split())
	indices = [*map(lambda x: int(x)-1, input().split())]

	q = deque(range(n))

	answer = 0

	for idx in indices:
		
		left = q.index(idx)
		right = len(q)-q.index(idx)
		
		if left < right:
			q.rotate(-left)
			answer += left
		else:
			q.rotate(right)
			answer += right

		q.popleft()

	print(answer)


solve()
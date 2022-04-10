n, m = map(int, input().split())
ans = []

def solution(idx):
	if len(ans) == m:
		print(*ans)
		return
	for i in range(1, n+1):
		if (i not in ans) and (i > idx):
			ans.append(i)
			solution(i)
			ans.pop()

solution(0)
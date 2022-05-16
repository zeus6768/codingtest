def solution():
	n, k = map(int, input().split())
	arr = list(range(1, n+1))
	answer = []
	idx = 0
	while arr:
		idx = (idx+k-1) % len(arr)
		answer.append(str(arr.pop(idx)))
	print("<" + ", ".join(answer) + ">")

solution()

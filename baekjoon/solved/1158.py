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


# idx 순서
# 2 -> 4 -> 1 -> 3 -> 2 -> 0
# length 변화
# 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1
# 1) [1 2 3 4 5 6 7]
# 2) [1 2 4 5 6 7] 2:3 삭제
# 3) [1 2 4 5 7] 4:6 삭제
# 4) [1 4 5 7] 1:2 삭제
# 5) [1 4 5] 3:7 삭제
# 6) [1 4] 2:5 삭제
# 7) [4] 0:1 삭제
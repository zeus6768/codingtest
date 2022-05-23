
def solution():
	n, l = map(int, input().split())
	height = sorted([*map(int, input().split())])

	for h in height:
		if h <= l:
			l += 1
		else:
			break
	print(l)

solution()

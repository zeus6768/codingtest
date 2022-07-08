from itertools import combinations as cb
def solve():
	while True:
		k, *S = input().split()
		if k == '0': break
		[print(" ".join(s)) for s in cb(S, 6)]
		print()

solve()
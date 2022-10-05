def solve():
	input()
	A = {*map(int, input().split())}
	B = {*map(int, input().split())}
	C = A.difference(B).union(B.difference(A))
	print(len(C))

solve()
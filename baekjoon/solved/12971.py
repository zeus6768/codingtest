def solve():
	N = x1
	while N < p1*p2*p3:
		if N%p1==x1 and N%p2==x2 and N%p3==x3:
			print(N)
			return
		N += p1
	print(-1)

if __name__ == "__main__":
	p1, p2, p3, x1, x2, x3 = map(int, input().split())
	solve()
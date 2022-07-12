def solve():
	n = int(input())
	q, r = n//5, n%5
	if r:
		while r % 2 and q:
			q -= 1
			r += 5
		print(-1) if r%2 else print(q+r//2)
	else:
		print(q)

solve()
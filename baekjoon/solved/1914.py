def solve():
	n = int(input())

	def hanoi_route(n, _from=1, _to=3, _via=2):
		if n == 1:
			print(_from, _to)
		else:
			hanoi_route(n-1, _from, _via, _to)
			print(_from, _to)
			hanoi_route(n-1, _via, _to, _from)

	print(2**n-1)
	hanoi_route(n)

solve()
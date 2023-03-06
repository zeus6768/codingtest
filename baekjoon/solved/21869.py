def f(n):
	if n == 1:
		return n
	return n + n -2

def g(n):
	first = [(1, i) for i in range(1, n+1)]
	last = [(n, i) for i in range(2, n)]
	return first + last


def main():
	N = int(input())
	print(f(N))
	[print(*a) for a in g(N)]

main()
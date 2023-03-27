def visit(n, r, c):
	if n == 1:
		return r*2+c
	if r < 2**(n-1) and c < 2**(n-1):
		sector = 0
	elif r < 2**(n-1) and c >= 2**(n-1):
		sector = 1
	elif r >= 2**(n-1) and c < 2**(n-1):
		sector = 2
	else:
		sector = 3
	return 2**(2*(n-1))*sector + visit(n-1, r%(2**(n-1)), c%(2**(n-1)))

if __name__ == "__main__":
	N, r, c = map(int, input().split())
	answer = visit(N, r, c)
	print(answer)


"""
N=3일 경우 8*8, 0~63 방문
N(n, r, c)
>>> 1) N(3, 7, 6) => 48 접근 => 48=16*3 => 2**(2*(n-1))*3
3은 어떻게 결정?? r >= 2**(n-1) and c >= 2**(n-1)
>>> 2) N(2, 7%4, 7%4) => 60 접근
>>> 3) N(1, 7%4%2, 7%4%2) => 62 접근
전체 넓이
1 -> 2**(2*1) -> 4
2 -> 2**(2*2) -> 16
3 -> 2**(2*3) -> 64
4 -> 2**(2*4) -> 256

"""
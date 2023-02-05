def ceil(number: float):
	if number <= int(number):
		return int(number)
	return int(number) + 1

def solve():
	H, W, N, M = map(int, input().split())
	print(ceil(H/(N+1)) * ceil(W/(M+1)))
	
solve()
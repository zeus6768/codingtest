def substr(string, idx):
	size = len(string)
	result = {string[i:i+idx] for i in range(size-idx+1)}
	return len(result)

def solve():
	S = input()
	answer = sum([substr(S, i) for i in range(1, len(S)+1)])
	print(answer)

solve()
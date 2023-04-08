def solve():
	answer = 0
	idx, count = 0, 0
	while idx < M:
		if S[idx:idx+3] == "IOI":
			count += 1
			idx += 1
		else:
			if N <= count:
				answer += count-N+1
			count = 0
		idx += 1
	print(answer)

if __name__ == "__main__":
	N = int(input())
	M = int(input())
	S = input()
	
	solve()
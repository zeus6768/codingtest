def input():
	return __import__('sys').stdin.readline()

def football(idx):
	global answer
	answer = min(answer, get_ability())
	for i in range(idx, N):
		selected[i] = True
		football(i+1)
		selected[i] = False

def get_ability():
	start, link = 0, 0
	for i in range(N):
		for j in range(i+1, N):
			if selected[i] and selected[j]:
				start += S[i][j] + S[j][i]
			if not selected[i] and not selected[j]:
				link += S[i][j] + S[j][i]
	return abs(start-link)

if __name__ == "__main__":
	N = int(input())
	S = [tuple(map(int, input().split())) for _ in range(N)]
	selected = [False] * N
	answer = float('inf')
	football(0, 0)
	print(answer)

"""
1 234
2 134
3 124
4 123
12 34
13 24
14 23

"""
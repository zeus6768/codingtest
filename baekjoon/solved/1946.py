import sys

def input():
	return sys.stdin.readline()

def solve():
	answer = N
	prev = applicants[0][1]
	for i in range(1, N):
		if prev < applicants[i][1]:
			answer -= 1
		else:
			prev = applicants[i][1]
	print(answer)

if __name__ == "__main__":
	T = int(input())
	for _ in range(T):
		N = int(input())
		applicants = sorted(tuple(map(int, input().split())) for _ in range(N))
		solve()
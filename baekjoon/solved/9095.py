import sys
sys.setrecursionlimit(60_000)

def input():
	return sys.stdin.readline()

def main():
	global answer
	n = int(input())
	answer = 0
	ways_of_sum(0, n)
	print(answer)

def ways_of_sum(now, n):
	global answer
	if now == n:
		answer += 1
		return
	for i in range(1, 4):
		if now+i <= n:
			ways_of_sum(now+i, n)
	return

if __name__ == "__main__":
	T = int(input())
	global answer
	[main() for _ in range(T)]

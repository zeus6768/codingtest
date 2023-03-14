import sys
sys.setrecursionlimit(1_000_000)

def input():
	return sys.stdin.readline()

def main() -> None:
	for _ in range(M):
		S, E = map(lambda x: int(x)-1, input().split())
		answer = is_palindrome(S, E)
		print(answer)

def is_palindrome(s:int, e:int) -> int:
	if dp[s][e] != -1:
		return dp[s][e]
	if e-s > 0:
		prev = is_palindrome(s+1, e-1)
		if prev and numbers[s] == numbers[e]:
			dp[s][e] = 1
		else:
			dp[s][e] = 0
		return dp[s][e]
	else:
		return 1

N = int(input())
numbers = list(map(int, input().split()))
M = int(input())

dp = [[-1]*N for _ in range(N)]

main()
import sys
input = sys.stdin.readline

def solve():

	def recursion(s, l, r):
		answer[1] += 1
		if r <= l:
			return 1
		elif s[l] != s[r]:
			return 0
		else:
			return recursion(s, l+1, r-1)

	def isPalindrome(s):
		return recursion(s, 0, len(s)-1)

	for _ in range(int(input())):
		S = input().strip()

		answer = [0, 0]

		answer[0] = isPalindrome(S)

		print(*answer)


solve()
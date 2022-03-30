import sys
input = sys.stdin.readline

def main():
	n = int(input())
	dp = [0] * (n+3)
	dp[1], dp[2], dp[3] = 1, 2, 1
	for i in range(4, n+1):
		if dp[i-1] == 2 or dp[i-3] == 2:
			dp[i] = 1
		else:
			dp[i] = 2

	print("SK") if dp[n]==1 else print("CY")

main()

# 다른 풀이
print(int(input())%2 and "SK" or "CY")
def main():
    h, n = map(int, input().split())
    l = abs(h-n)
    dp = [[1] * (l+1) for _ in range(l+1)]

    if h == n:
        print(1)
    else:
        for i in range(l+1):
            for j in range(l+1):
                if i == 0:
                    dp[i][j] = 1
                elif i > j:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        print(max(dp[-1]))

main()
def main():
    h, y = map(int, input().split())

    dp = [h] * (y+1)

    for i in range(1, y+1):
        if i < 3:
            dp[i] = int(dp[i-1]*1.05)
        elif i < 5:
            dp[i] = max(int(dp[i-1]*1.05), int(dp[i-3]*1.2))
        else:
            dp[i] = max(int(dp[i-1]*1.05), int(dp[i-3]*1.2), int(dp[i-5]*1.35))

    print(dp[y])

main()
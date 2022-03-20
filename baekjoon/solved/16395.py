def main():
    n, k = map(int, input().split())
    arr = [[1]*i for i in range(1, n+1)]

    for i in range(2, n):
        for j in range(1, i):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print(arr[n-1][k-1])

main()
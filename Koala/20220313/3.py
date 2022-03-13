from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    candies = [list(input().rstrip()) for _ in range(n)]

    # 교환
    f = False
    for i in range(n-1):
        if f:
            break
        for j in range(n-1):
            if (candies[i][j] != candies[i][j+1]):
                candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]
                f = True
                break
            elif (candies[i][j] != candies[i+1][j]):
                candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]
                f = True
                break
            
    # 탐색
    result = 0
    for i in range(n-1):
        for j in range(n-1):
            if (candies[i][j] == candies[i][j+1]) and (j == n-2):
                result += n
            elif candies[i][j] != candies[i][j+1]:
                break
            
    for i in range(n-1):
        for j in range(n-1):
            if (candies[j][i] == candies[j][i+1]) and (j == n-2):
                result += n
            elif candies[j][i] != candies[j][i+1]:
                break

    print(result)

main()
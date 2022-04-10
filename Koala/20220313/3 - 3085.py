from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    candies = [list(input().rstrip()) for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(n-1):
            tmp = 0
            if candies[i][j] != candies[i][j+1]:
                candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]
                tmp = count(n, candies)
                if result < tmp:
                    result = tmp
                candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]

        for j in range(n-1):
            tmp = 0
            if candies[j][i] != candies[j+1][i]:
                candies[j][i], candies[j+1][i] = candies[j+1][i], candies[j][i]
                tmp = count(n, candies)
                if result < tmp:
                    result = tmp
                candies[j][i], candies[j+1][i] = candies[j+1][i], candies[j][i]
    print(result)
    

def count(n, candies):
    result = 0
    for i in range(n):
        count = 1
        for j in range(n-1):
            if candies[i][j] == candies[i][j+1]:
                count +=1
            else:
                count = 1
            if result < count:
                result = count

        count = 1
        for j in range(n-1):
            if candies[j][i] == candies[j+1][i]:
                count +=1
            else:
                count = 1
            if result < count:
                result = count

    return result

main()

# correct

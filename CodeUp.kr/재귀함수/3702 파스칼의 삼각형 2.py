# import sys
# sys.setrecursionlimit(100000)

def pascal(x, y):
    global memo
    if x == 1 or y == 1:
        return 1
    
    elif memo[x][y]:
        return memo[x][y]

    result = pascal(x - 1, y) + pascal(x, y - 1)
    memo[x][y] = result

    return result

r, c = map(int, input().split())
memo = [[0] * (c + 1) for _ in range(r + 1)]

final_result = pascal(r, c) % 100000000
print(final_result)
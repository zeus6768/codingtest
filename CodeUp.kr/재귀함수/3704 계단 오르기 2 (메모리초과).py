import sys
sys.setrecursionlimit(100000)

def stairway(number):
    global memo

    if number <= 2:
        return number

    elif number == 3:
        return 4

    elif memo[number]:
        return memo[number]

    result = stairway(number - 1) + stairway(number - 2) + stairway(number - 3)
    memo[number] = result

    return result

n = int(input())
memo = [0] * (n + 1)

print(stairway(n) % 1000)
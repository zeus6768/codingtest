# 나의 풀이


# 다른 사람의 풀이

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

result = factorial(4)
print(result)
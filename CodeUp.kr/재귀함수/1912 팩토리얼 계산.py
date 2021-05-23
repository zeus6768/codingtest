def factorial(num):
    if num != 1:
        return num * factorial(num - 1)
    else:
        return 1

n = int(input())
result = factorial(n)
print(result)
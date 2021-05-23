def fibo(num):
    if num > 2:
        return fibo(num - 1) + fibo(num - 2)
    else:
        return 1

n = int(input())
result = fibo(n)
print(result)

# (1, 1, 2, 3, 5, 8, 13, 21, 34, ...)
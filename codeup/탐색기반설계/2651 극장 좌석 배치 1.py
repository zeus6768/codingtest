from sys import stdin
n, k = map(int, stdin.readline().split())
def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)

n_fac, nk_fact, k_fack = factorial(n), factorial(n - k), factorial(k)
result = int(n_fac / nk_fact / k_fack)
print(result)
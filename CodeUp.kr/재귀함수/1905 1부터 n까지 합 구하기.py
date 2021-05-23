import sys
sys.setrecursionlimit(100000)

def myfunc(num):
    if num != 1:
        return num + myfunc(num - 1)
    else:
        return 1

n = int(input())

result = myfunc(n)
print(result)
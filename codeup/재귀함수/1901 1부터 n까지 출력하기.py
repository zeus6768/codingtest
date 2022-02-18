def myfunc(num):
    if num != 1:
        myfunc(num - 1)
    print(num)

n = int(input())
myfunc(n)
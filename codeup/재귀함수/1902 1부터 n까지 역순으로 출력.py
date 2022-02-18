def myfunc(num):
    print(num)
    if num != 1:
        myfunc(num - 1)

n = int(input())
myfunc(n)
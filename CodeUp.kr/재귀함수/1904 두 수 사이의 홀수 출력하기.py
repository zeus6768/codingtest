def myfunc(a, b):
    if a > b:
        return
    elif a % 2:
        print(a, end = ' ')
    myfunc(a + 1, b)

a, b = map(int, input().split())
myfunc(a, b)
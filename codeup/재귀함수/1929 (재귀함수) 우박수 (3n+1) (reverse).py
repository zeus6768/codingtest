def myfunc(number):
    if number == 1:
        print(number)
    elif number % 2:
        myfunc(3 * number + 1)
        print(number)
    else:
        myfunc(number // 2)
        print(number)

n = int(input())
myfunc(n)
def myfunc(number):
    if number == 1:
        return number
    elif number % 2:
        print(number)
        return myfunc(3 * number + 1)
    else:
        print(number)
        return myfunc(number // 2)

n = int(input())
print(myfunc(n))
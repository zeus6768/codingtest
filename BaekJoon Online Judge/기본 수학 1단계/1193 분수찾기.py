""" def a_n(num):
    return 2 * (num - 1) ** 2 + 3 * (num - 1) + 1
def n_compare_A(A):
    i = 0
    while True:
        i += 1
        if a_n(i) <= A < a_n(i + 1):
            return i 
def result(A):
    n = n_compare_A(A)
    if A == a_n(n):
        print("%d/%d" % (1, 2 * n - 1))
    elif A - a_n(n) <= 2 * n:
        print("%d/%d" % (A - a_n(n), 2 * n + 1 - A + a_n(n)))
    else:
        print("%d/%d" % (4 * n + 2 - A + a_n(n), A - a_n(n) - 2 * n))
x = int(input())
result(x) """


'''입력
1) 1
>>> 1/1
2) 2
>>> 1/2
3) 3
>>> 2/1
4) 4
>>> 3/1
5) 5
>>> 2/2
6) 6
>>> 1/3
7) 7
>>> 1/4

'''

# 다른 풀이
# x = int(input())
# fx = -int(-((8*x+1)**0.5-3)//2)
# gx = (fx**2+3*fx+2)//2          
# rep = gx - x
# print(f"{fx-rep+1}/{rep+1}" if fx % 2 else f"{rep+1}/{fx-rep+1}")


# 지수 풀이
n = int(input())
sum = -int((-(8*n-1)**0.5-1)//2)
order = 0
if sum == 2 : print("1/1")
else : 
    while -int((-(8*(n-order)-1)**0.5-1)//2) == sum : order += 1
    print(str(order)+"/"+str(sum-order) if sum % 2 else str((sum-order))+"/"+str(+order))
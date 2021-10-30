import sys
n = int(sys.stdin.readline().rstrip())
x_n = list(map(int, sys.stdin.readline().rstrip().split()))
set_x_n = sorted(list(set(x_n)))
dic_x_n = {set_x_n[i]: i for i in range(len(set_x_n))}
[print(dic_x_n[j], end=" ") for j in x_n]
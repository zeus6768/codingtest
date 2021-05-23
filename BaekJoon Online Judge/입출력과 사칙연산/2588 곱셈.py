from sys import stdin
in_arr = [stdin.readline() for _ in range(2)]
[print(int(in_arr[0]) * int(in_arr[1][i])) for i in range(2, -1, -1)]
print(int(in_arr[0]) * int(in_arr[1]))
from sys import stdin
n, x = map(int, stdin.readline().split())
array_A = list(map(int, stdin.readline().split()))

for num in array_A:
    if num < x:
        print(num, end = ' ')
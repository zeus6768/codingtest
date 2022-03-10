from sys import stdin
from itertools import permutations as pm

input = stdin.readline

n, m = map(int, input().split())
[print(*a) for a in pm([i+1 for i in range(n)], m)]

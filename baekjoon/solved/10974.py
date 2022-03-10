from sys import stdin
from itertools import permutations as pm
input = stdin.readline

n = int(input())
p = pm([i+1 for i in range(n)])
[print(*j) for j in p]

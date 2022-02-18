import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
info1 = {}
for i in range(N):
	name, place, start, end = input().split()
	start, end = int(start), int(end)
	if name in info1:
		continue
	else:
		info1[name] = (place, start, end)

info2 = {}
for n in info1: info2[info1[n][0]] = (info1[n][1], info1[n][1])

info3 = {}
for pl in info2: info3[pl] = info3[pl]+1 if pl in info3 else 1

print(info3)
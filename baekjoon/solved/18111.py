from sys import stdin
from collections import Counter
input = stdin.readline

def main():
	ground, time = [], {}
	n, m, b = map(int, input().split())
	[ground.extend(list(map(int, input().split()))) for _ in range(n)]
	ground_counter = Counter(ground)
	for g in range(257):
		block = b
		time[g] = 0
		for h in ground_counter:
			cost = abs(g-h)*ground_counter[h]
			if g < h: # op1, pop
				time[g] += cost * 2
				block += cost
			elif g > h: # op2, push
				time[g] += cost
				block -= cost
		if (block < 0):
			time[g] = float("inf")

	time = sorted(list(zip(time.keys(), time.values())), key=lambda x: (x[1], -x[0]))
	print(time[0][1], time[0][0])

main()
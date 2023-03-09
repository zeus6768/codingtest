from itertools import permutations as pm

def input():
	return __import__('sys').stdin.readline()

def main():
	for _ in range(N):
		num, strike, ball = input().split()
		num, strike, ball = tuple(num), int(strike), int(ball)
		for number in NUMBERS:
			if count(num, number) != (strike, ball) and number in COMPARE:
				COMPARE.remove(number)
	print(len(COMPARE))

def count(num, goal):
	s, b = 0, 0
	for i in range(3):
		s += num[i] == goal[i]
		b += num[i] != goal[i] and num[i] in goal
	return s, b

N = int(input())
NUMBERS = set(pm('123456789', 3))
COMPARE = NUMBERS.copy()

main()

import sys

def input():
	return sys.stdin.readline()

def num_of_outliers(n: int):
	return round(n * 0.15)

def round(n: float):
	if int(n) + 0.5 <= n:
		return int(n)+1
	return int(n)

def average(nums: list):
	return round(sum(nums) / len(nums)) if nums else 0

N = int(input())
user_opinions = sorted(int(input()) for _ in range(N))
outliers = num_of_outliers(N)
level = average(user_opinions[outliers:N-outliers])

print(level)

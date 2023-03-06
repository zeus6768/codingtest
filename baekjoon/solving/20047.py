from sys import stdin

def input():
	return stdin.readline()

def main():
	
	n = int(input())
	S = input()
	T = input()
	i, j = map(int, input().split())

	dp = [[0] * n for _ in range(3)]
	


from sys import stdin



def input():
	return stdin.readline()

def main():

	N = int(input())
	operands = [int(input()) for _ in range(N)]
	operators = [int(input()) for _ in range(N-1)]


	return
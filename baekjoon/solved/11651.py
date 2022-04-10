import sys
input = sys.stdin.readline

def main():
	n = int(input())
	xy = [[*map(int, input().split())] for _ in range(n)]
	xy = sorted(xy, key=lambda x: (x[1], x[0]))
	[print(x[0], x[1]) for x in xy]

main()
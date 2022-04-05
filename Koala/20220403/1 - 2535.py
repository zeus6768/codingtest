import sys
input = sys.stdin.readline

def main():
	n = int(input())
	arr = [[*map(int, input().split())] for _ in range(n)]
	arr = sorted(arr, key=lambda x: -x[2])
	result = [(arr[0][0], arr[0][1]), (arr[1][0], arr[1][1])]
	if result[0][0] == result[1][0]:
		for i in range(2, n):
			if arr[i][0] != result[0][0]:
				result.append((arr[i][0], arr[i][1]))
				break
	else:
		result.append((arr[2][0], arr[2][1]))
	[print(*r) for r in result]

main()
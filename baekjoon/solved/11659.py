import sys
input = sys.stdin.readline
def main():
	n, m = map(int, input().split())
	arr = [*map(int, input().split())]
	sums = [0] * (n+1)

	for i in range(1, n+1):
		sums[i] = sums[i-1] + arr[i-1]

	for _ in range(m):
		i, j = map(int, input().split())
		result = sums[j] - sums[i-1]
		print(result)
main()
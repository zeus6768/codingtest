def input():
	return __import__('sys').stdin.readline()

def main():
	answer = 0

	left, right = 1, d
	while left <= right:
		mid = (left+right)//2
		now, count = 0, 0
		for i in range(n):
			if now + mid <= distances[i]:
				now = distances[i]
				count += 1
		if n-m <= count:
			left = mid + 1
			answer = mid
		else:
			right = mid - 1
	print(answer)

if __name__ == "__main__":
	d, n, m = map(int, input().split())
	distances = sorted(int(input()) for _ in range(n))
	main()
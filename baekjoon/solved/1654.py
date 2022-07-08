input = __import__('sys').stdin.readline

def main():
	k, n = map(int, input().split())
	arr = [int(input()) for _ in range(k)]
	l, r = 0, 2**31-1

	while l <= r:
		mid = (l + r) // 2
		value = 0
		for line in arr:
			value += line // mid
		if value < n:
			r = mid-1
		else:
			l = mid+1

	print(l-1)

main()
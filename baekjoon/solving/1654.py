def main():
	k, n = map(int, input().split())
	arr = [int(input()) for _ in range(k)]
	low, high = 0, 2**31

	while low+1 < high:
		mid = (low + high) // 2
		value = 0
		for line in arr:
			value += line // mid
		if value < n:
			high = mid
		else:
			low = mid

	print(low)

main()
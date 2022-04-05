import sys
input = sys.stdin.readline

def main():
	n, m = map(int, input().split())
	arr = [*map(int, input().split())]
	
	left, right = 1, 10**9
	result = float('inf')
	while left <= right:
		mid = (left+right)//2
		blueray, blueraynum = 0, 1
		for a in arr:
			if blueray + a <= mid:
				blueray += a
			elif a > mid:
				blueraynum = float('inf')
				break
			else:
				blueraynum += 1
				blueray = a
		if blueraynum <= m:
			result = min(result, mid)
			right = mid-1
		else:
			left = mid+1

	print(result)

main()
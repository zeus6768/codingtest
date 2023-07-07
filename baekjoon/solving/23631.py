import sys

def input():
	return sys.stdin.readline()


def solve():
	T = int(input())
	for _ in range(T):
		N, K = map(int, input().split())
		
		left, right = 0, 3161
		while left <= right:
			mid = (left+right) // 2
			total = c_sum[mid]*K
			if total < N:
				left = mid + 1
			else:
				right = mid - 1
		print(mid, total)
		if mid % 2:
			now = -K * (mid//2+1)
			direction = 'R'
		else:
			now = K * (mid//2+1)
			direction = 'L'
		now += (N-1) - total
		print(now, direction)



c_sum = [1]
[c_sum.append(c_sum[-1] + i) for i in range(2, 3163)]
# print(c_sum[3161])

solve()
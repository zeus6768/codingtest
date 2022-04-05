import sys
input = sys.stdin.readline

def main():
	n = int(input())
	server_room = sorted(sum([list(map(int, input().split())) for _ in range(n)], []))
	half = sum(server_room)/2
	left, right, mid = 0, server_room[-1], 0
	answer = float('inf')
	while left <= right:
		mid = (left+right)//2
		count = 0
		for com_num in server_room:
			if com_num:
				count += com_num if com_num <= mid else mid
		if count >= half:
			answer = mid if mid < answer else answer
			right = mid-1
		else:
			left = mid+1
	print(answer)

main()
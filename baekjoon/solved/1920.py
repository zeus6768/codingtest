import sys
input = sys.stdin.readline

# 이진탐색
def main():
	n = int(input())
	A = sorted(map(int, input().split()))
	m = int(input())
	nums = [*map(int, input().split())]

	for num in nums:
		left, right = 0, len(A)-1
		mid = len(A) // 2
		while True:
			if num == A[mid]:
				print(1)
				break
			elif (left == mid) or (right == mid):
				if (num == A[left]) or (num == A[right]):
					print(1)
				else:
					print(0)
				break
			elif num < A[mid]:
				right = mid
				mid = (left+right) // 2
			elif num > A[mid]:
				left = mid
				mid = (left+right) // 2
		
main()

# 더 간단한 풀이
input = __import__('sys').stdin.readline
input()
A = set(input().split())
input()
M = input().split()
print("\n".join(['1' if i in A else '0' for i in M]))
#[print(1) if i in A else print(0) for i in M]
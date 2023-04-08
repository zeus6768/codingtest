import sys
sys.setrecursionlimit(10**6)

def compare(left, right):

	if left == N or right == N:
		return 0
	
	if scores[left][right] != -1:
		return scores[left][right]
	
	if A[left] > B[right]:
		scores[left][right] = compare(left, right+1) + B[right]
	else:
		scores[left][right] = max(compare(left+1, right), compare(left+1, right+1))
	
	return scores[left][right]

if __name__ == "__main__":
	N = int(input())
	A = tuple(map(int, input().split()))
	B = tuple(map(int, input().split()))

	scores = [[-1]*N for _ in range(N)]
	answer = compare(0, 0)
	print(answer)
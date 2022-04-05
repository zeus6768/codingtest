import sys
input = sys.stdin.readline

def main():
	n, m = map(int, input().split())
	tree = sorted(map(int, input().split()))
	left, right = 1, tree[-1]
	mid = right//2
	result = 0
	while mid != left:
		h = [t-mid for t in tree if (t-mid)>0]
		add = sum(h)
		if add == m:
			result = mid
			break
		elif add > m:
			result = mid
			left = mid
			mid = (left+right)//2
		else:
			right = mid
			mid = (left+right)//2
	
	print(result)

main()
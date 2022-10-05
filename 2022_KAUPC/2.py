import sys
input = sys.stdin.readline

def solve():
	relation = {}
	for _ in range(int(input())-1):
		child, parent = input().strip().split()
		if parent in relation:
			relation[parent].append(child)
		else:
			relation[parent] = [child]
		if child in relation:
			relation[child].append(parent)
		else:
			relation[child] = [parent]
	


	return


solve()
def input():
	return __import__('sys').stdin.readline()

def solve():
	_ = input()
	L = sorted(map(int, input().split()))
	L = get_best_array(L)
	answer = get_max_diff(L)
	print(answer)

def get_max_diff(trees):
	size = len(trees)
	r = 0
	for i in range(size):
		r = max(r, abs(trees[i]-trees[(i+1)%size]))
	return r

def get_best_array(trees):
	size = len(trees)
	new_trees = [0]*size
	l, r = 0, size-1
	for i in range(size):
		if i % 2:
			new_trees[r] = trees[i]
			r -= 1
		else:
			new_trees[l] = trees[i]
			l += 1
	return new_trees

if __name__ == "__main__":
	T = int(input())
	[solve() for _ in range(T)]
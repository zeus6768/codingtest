from itertools import permutations as pm

def input():
	return __import__('sys').stdin.readline()

def main():
	board = [[0 for _ in range(min_y, max_y)] for _ in range(min_x, max_x)]
	answer = [0]
	print(board)
	# print(*answer)
	return

# def get_mass_center(indices):
# 	size = len(indices)
# 	cx, cy = 0, 0
# 	for idx in indices:
# 		cx += board[idx][0]
# 		cy += board[idx][1]
# 	cx /= size
# 	cy /= size
# 	return round(cx), round(cy)

def get_rectangular_distance(source, destination):
	return abs(source[0]-destination[0]) + abs(source[1]-destination[1])

N = int(input())
checkers = []
min_x, min_y, max_x, max_y = float('inf'), float('inf'), 0, 0
for _ in range(N):
	x, y = map(int, input().split())
	min_x, min_y, max_x, max_y = min(min_x, x), min(min_y, y), max(max_x, x), max(max_y, y)

main()
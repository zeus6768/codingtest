n, m = map(int, input().split())
chess_board = [list(input()) for _ in range(n)]

def sum_of_2d_list(list2d: list) -> int:
	result = 0
	for list in list2d:
		result += sum(list)
	return result

def count_rect(board_8by8):
	for i in range(8):
		for j in range(8):
			if (i + j) % 2 == board_8by8[i][j]:
				board_8by8[i][j] = 0
			else:
				board_8by8[i][j] = 1
	num_of_rect_to_change = sum_of_2d_list(board_8by8)
	return min(n*m - num_of_rect_to_change, num_of_rect_to_change)

def result(board_nbyn):
	n = len(board_nbyn)
	for i in range(n-8+1):
		pass
	return

import sys
input = sys.stdin.readline

def sudoku():
	table = [[*map(int, input().split())] for _ in range(9)]
	blank = [(i, j) for j in range(9) for i in range(9) if table[i][j]==0]
	
	def checkRow(r, x):
		for i in range(9):
			if x == table[r][i]:
				return False
		return True

	def checkCol(c, x):
		for i in range(9):
			if x == table[i][c]:
				return False
		return True

	def checkSquare(r, c, x):
		nr, nc = r//3*3, c//3*3
		for i in range(3):
			for j in range(3):
				if table[nr+i][nc+j] == x:
					return False
		return True

	def fill(idx):
		if idx == len(blank):
			[print(*table[i]) for i in range(9)]
			exit()
		
		for i in range(1, 10):
			r = blank[idx][0]
			c = blank[idx][1]
			if checkRow(r, i) and checkCol(c, i) and checkSquare(r, c, i):
				table[r][c] = i
				fill(idx+1)
				table[r][c] = 0
	fill(0)
	

sudoku()
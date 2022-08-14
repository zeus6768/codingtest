import sys
input = sys.stdin.readline

def solve():
	n = int(input())
	classroom = [[0]*n for _ in range(n)]
	students = {}
	dxy = ((-1, 0), (0, -1), (1, 0), (0, 1))
	for _ in range(n**2):
		a, *b =  list(map(int, input().split()))
		students[a] = b

	def condition1(student):
		seats = []
		_max = 0
		for i in range(n):
			for j in range(n):
				if classroom[i][j]==0:
					tmp = 0
					for k in range(4):
						nr, nc = i+dxy[k][0], j+dxy[k][1]
						if (0<=nr<n) and (0<=nc<n) and (classroom[nr][nc] in students[student]):
							tmp += 1
					if _max < tmp:
						seats = [(i, j)]
						_max = tmp
					elif _max == tmp:
						seats.append((i, j))
		return seats

	def condition2(seats):
		x, y = seats[0]
		_max = 0
		for r, c in seats:
			tmp = 0
			for i in range(4):
				nr, nc = r+dxy[i][0], c+dxy[i][1]
				if (0<=nr<n) and (0<=nc<n) and (classroom[nr][nc]==0):
					tmp += 1
			if _max < tmp:
				x, y = r, c
				_max = tmp
		return x, y

	def satisfy():
		result = 0
		for i in range(n):
			for j in range(n):
				score = 0
				student = classroom[i][j]
				for k in range(4):
					nr, nc = i+dxy[k][0], j+dxy[k][1]
					if (0<=nr<n) and (0<=nc<n) and (classroom[nr][nc] in students[student]):
						score += 1
				result += 10**(score-1) if score else 0
		return result

	for student in students:
		seats = condition1(student)
		seat = condition2(seats)
		classroom[seat[0]][seat[1]] = student

	answer = satisfy()
	print(answer)

solve()
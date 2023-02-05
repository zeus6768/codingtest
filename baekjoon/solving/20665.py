from sys import stdin
input = stdin.readline

def convert_hhmm_to_mmm(hhmm: str):
	return (int(hhmm[:2]) - 9) * 60 + int(hhmm[2:])

def select_seat(seats: list):

	x, y = 0, 0

	size = len(seats)
	tmp = [[0, 0] for _ in range(size)]

	for i in range(size):
		if seats[i]:
			x = 0
		if not seats[i]:
			x += 1
		if seats[size-1-i]:
			y = 0
		if not seats[size-1-i]:
			y += 1

		tmp[i][0] += x
		tmp[size-1-i][1] += y

	distance = list(map(min, tmp))
	distance[0] = tmp[0][1]
	distance[-1] = tmp[-1][0]

	return distance.index(max(distance))

def solve():

	PM_09 = "2100"
	OPEN_FOR = convert_hhmm_to_mmm(PM_09)	# 12 hours = 720 minutes

	N, T, P = map(int, input().split())
	times = sorted(tuple(map(convert_hhmm_to_mmm, input().split())) for _ in range(T))
	
	selected = [[False] * N for _ in range(OPEN_FOR+1)]
	
	for start, end in times:
		seat = select_seat(selected[start])
		for t in range(start, end):
			selected[t][seat] = True

	answer = 0
	for i in range(OPEN_FOR):
		if not selected[i][P-1]:
			answer += 1

	print(answer)

solve()

# array = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# r = select_seat(array)
# print(r)

'''
5 6 1
0915 0930
0940 2040
0910 0920
0915 0930
2043 2047
2044 20461
'''
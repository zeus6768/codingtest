from itertools import permutations

def calc(matrix):
	case1 = sum(matrix[:3])
	case2 = sum(matrix[3:6])
	case3 = sum(matrix[6:9])
	case4 = matrix[0]+matrix[3]+matrix[6]
	case5 = matrix[1]+matrix[4]+matrix[7]
	case6 = matrix[2]+matrix[5]+matrix[8]
	case7 = matrix[0]+matrix[4]+matrix[8]
	case8 = matrix[2]+matrix[4]+matrix[6]
	return case1 == case2 == case3 == case4 == case5 == case6 == case7 == case8

def solve():
	matrix = [*map(int, input().split())]
	answer = False

	for idices in permutations(range(1, 10)):
		new_matrix = [matrix[i-1] for i in idices]
		answer = calc(new_matrix)
		if answer:
			print("YES")
			return

	print("NO")

solve()


"""
1 2 3 
4 5 6 
7 8 9

100 1000 ... 1000000
"""
def solve():

	N = int(input())
	skills = input()

	L, S = 0, 0

	answer = 0
	
	for skill in skills:
		if skill.isdigit():
			answer += 1
		elif skill == 'L':
			L += 1
		elif skill == 'R' and L:
			L -= 1
			answer += 1
		elif skill == 'S':
			S += 1
		elif skill == 'K' and S:
			S -= 1
			answer += 1
		elif (skill == 'R' and L == 0) or (skill == 'K' and S == 0):
			break
	
	print(answer)


solve()
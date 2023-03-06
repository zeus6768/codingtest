def solve():

	def zero():
		display = [[' '] * (s+2) for _ in range(2*s+3)]
		for i in range(s):
			display[0][1+i] = H
			display[-1][1+i] = H
		for i in range(1, s+1):
			display[i][0] = V
			display[i][-1] = V
			display[s+1+i][0] = V
			display[s+1+i][-1] = V
		return display
	
	def one():
		display = [[' '] * (s+2) for _ in range(2*s+3)]
		for i in range(1, s+1):
			display[i][-1] = V
			display[s+1+i][-1] = V
		return display
	
	def two():
		display = [[' '] * (s+2) for _ in range(2*s+3)]
		for i in range(s):
			for j in range(3):
				display[(s+1)*j][1+i] = H
		for i in range(1, s+1):
			display[i][-1] = V
			display[s+1+i][0] = V
		return display
	
	def three():
		display = [[' '] * (s+2) for _ in range(2*s+3)]
		for i in range(s):
			for j in range(3):
				display[(s+1)*j][1+i] = H
		for i in range(1, s+1):
			display[i][-1] = V
			display[s+1+i][-1] = V
		return display

	def four():
		display = [[' '] * (s+2) for _ in range(2*s+3)]
		for i in range(s):
			display[s+1][1+i] = H
		for i in range(1, s+1):
			display[i][0] = V
			display[i][-1] = V
			display[s+1+i][-1] = V
		return display
	
	def five():
		display = [[' '] * (s+2) for _ in range(2*s+3)]
		for i in range(s):
			for j in range(3):
				display[(s+1)*j][1+i] = H
		for i in range(1, s+1):
			display[i][0] = V
			display[s+1+i][-1] = V
		return display
	
	def six():
		display = [[' '] * (s+2) for _ in range(2*s+3)]
		for i in range(s):
			for j in range(3):
				display[(s+1)*j][1+i] = H
		for i in range(1, s+1):
			display[i][0] = V
			display[s+1+i][0] = V
			display[s+1+i][-1] = V
		return display

	def seven():
		display = [[' '] * (s+2) for _ in range(2*s+3)]
		for i in range(s):
			display[0][1+i] = H
		for i in range(1, s+1):
			display[i][-1] = V
			display[s+1+i][-1] = V
		return display
	
	def eight():
		display = [[' '] * (s+2) for _ in range(2*s+3)]
		for i in range(s):
			for j in range(3):
				display[(s+1)*j][1+i] = H
		for i in range(1, s+1):
			display[i][0] = V
			display[i][-1] = V
			display[s+1+i][0] = V
			display[s+1+i][-1] = V
		return display
	
	def nine():
		display = [[' '] * (s+2) for _ in range(2*s+3)]
		for i in range(s):
			for j in range(3):
				display[(s+1)*j][1+i] = H
		for i in range(1, s+1):
			display[i][0] = V
			display[i][-1] = V
			display[s+1+i][-1] = V
		return display
	
	def add(list1, list2):
		if (list1 == BLANK) or (list2 == BLANK):
			return [list1[i]+list2[i] for i in range(len(list1))]
		return [list1[i]+BLANK[i]+list2[i] for i in range(len(list1))]
	
	def display(number: str):
		numbers = (zero, one, two, three, four, five, six, seven, eight, nine)
		return numbers[int(number)]()
	
	s, n = input().split()
	s = int(s)

	H, V = '-', '|'
	BLANK = [[' '] for _ in range(2*s+3)]
	answer = display(n[0])
	for i in range(1, len(n)):
		answer = add(answer, display(n[i]))
	answer = add(answer, BLANK)
	answer = ["".join(a) for a in answer]
	[print(d) for d in answer]

solve()
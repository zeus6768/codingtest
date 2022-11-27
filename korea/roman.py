def solve():
	
	chars = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, 
			"I": 1, "V": 5, "X": 10, "L": 50, "C": 100}
	
	string = input()
	answer = 0

	while string:
		tmp = string[:2]
		if tmp in chars:
			answer += chars[tmp]
			string = string[2:]
		else:
			tmp = string[0]
			answer += chars[tmp]
			string = string[1:]

	print(answer)

solve()
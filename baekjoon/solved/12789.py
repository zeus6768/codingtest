def solution():
	n = int(input())
	students = [*map(int, input().split())]
	now, stack = 1, []
	while students or stack:
		if students and (students[0] == now):
			students.pop(0)
			now += 1
		elif stack and (stack[-1] == now):
			stack.pop()
			now += 1
		else:
			if stack and (stack[-1] < students[0]):
				print("Sad")
				exit()
			else:
				stack.append(students.pop(0))
	print("Nice")

solution()
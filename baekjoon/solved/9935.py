import sys
input = sys.stdin.readline

def solve():
	
	string = input().strip()
	sub_str = input().strip()

	size1, size2 = len(string), len(sub_str)
	stack = list()

	for i in range(size1):
		stack.append(string[i])
		if "".join(stack[-size2:]) == sub_str:
			for _ in range(size2):
				stack.pop()
	
	answer = "".join(stack)
	print(answer) if answer else print('FRULA')

solve()
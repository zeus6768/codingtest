def solution():
	while True:
		sen = input()
		if sen == '.':
			break
		else:
			print('yes') if balance(sen) else print('no')

def balance(sen):
	stack = []
	for s in sen:
		if s == '(' or s == '[':
			stack.append(s)
		elif s == ')':
			if stack and stack[-1] == '(':
				stack.pop()
			else:
				return False
		elif s == ']':
			if stack and stack[-1] == '[':
				stack.pop()
			else:
				return False
	return not bool(stack)

solution()
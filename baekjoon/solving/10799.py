def solve():
	batch = input()
	stack = 0
	answer = 0
	for i in range(len(batch)):
		if batch[i] == '(':
			if batch[i+1] == ')':
				answer += stack
			else:
				stack += 1
		else:
			if batch[i-1] == '(':
				continue
			else:
				stack -= 1
				answer += 1
	print(answer)


# 풀이 2 
def solve2():
	batch = input().split('()')

	answer = 0
	stack = 0
	for b in batch:
		closeCnt = b.count(')')
		stack += len(b) -2*closeCnt
		answer += stack+closeCnt
	print(answer)

solve2()
import sys
input = sys.stdin.readline

def solve():
	n = int(input())
	exp = input().strip()
	values = [int(input()) for _ in range(n)]

	dic, idx = {}, 0
	for e in exp:
		if e.isalpha() and e not in dic:
			dic[e] = values[idx]
			idx += 1

	stack = []

	for e in exp:
		if e.isalpha():
			stack.append(dic[e])
		else:
			y = stack.pop()
			x = stack.pop()

			if e == '+':
				r = x + y
			elif e == '-':
				r = x - y
			elif e == '*':
				r = x * y
			else:
				r = x / y

			stack.append(r)

	print(f"{stack[0]:.2f}")

solve()
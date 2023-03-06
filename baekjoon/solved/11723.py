from sys import stdin

def input():
	return stdin.readline()

def main():

	M = int(input())
	
	S = 0b0
	OPCODE = ['add', 'remove', 'check', 'toggle', 'all', 'empty']

	for _ in range(M):

		operation = input().split()

		if len(operation) == 1:
			opcode = operation[0]
		if len(operation) == 2:
			opcode, x = operation[0], int(operation[1])

		if opcode == OPCODE[0]:
			S |= (1 << x)
		if opcode == OPCODE[1]:
			S &= (0 << x)
		if opcode == OPCODE[2]:
			print(1) if S & (1 << x) else print(0)
		if opcode == OPCODE[3]:
			S ^= (1 << x)
		if opcode == OPCODE[4]:
			S = -1
		if opcode == OPCODE[5]:
			S = 0

main()

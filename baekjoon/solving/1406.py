import sys

def input():
	return sys.stdin.readline().strip()

string = input()
N = len(string)
M = int(input())

cursor = N

for _ in range(M):
	instruction = input()

	if instruction == 'L':
		if cursor > 0:
			cursor -= 1
	elif instruction == 'D':
		if cursor < N:
			cursor += 1
	elif instruction == 'B':
		if cursor > 0:
			string = string[:cursor-1] + string[cursor:]
			cursor -= 1
	else:
		instruction, letter = instruction.split()
		string = string[:cursor] + letter + string[cursor:]
		cursor += 1
	
print(string)

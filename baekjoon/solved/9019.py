from collections import deque

def input() -> str:
	return __import__('sys').stdin.readline()

def main() -> None:
	for _ in range(T):
		A, B = map(int, input().split())
		answer = bfs(A, B)
		print(answer)

def D(n):
	return n*2%10000

def S(n):
	return n-1 if n else 9999

def L(n):
	return n*10 if n < 1000 else n%1000*10 + n//1000

def R(n):
	d1, d2, d3, d4 = n//1000, n%1000//100, n%100//10, n%10
	return d4*1000 + d1*100 + d2*10 + d3

def bfs(a:int, b:int) -> str:
	instructions = {'D':D, 'S':S, 'L':L, 'R':R}
	result = set()
	queue = deque([(a, '')])
	while queue:
		value, op = queue.popleft()
		for inst in instructions:
			new_value = instructions[inst](value)
			if new_value == b:
				return op + inst
			elif new_value not in result:
				queue.append((new_value, op + inst))
				result.add(new_value)

T = int(input())

main()
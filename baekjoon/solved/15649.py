from sys import stdin
input = stdin.readline

def solution():
	n, m = map(int, input().split())

	answer = []
	def go():
		if len(answer) == m:
			print(*answer)
			return
		for i in range(1, n+1):
			if i not in answer:
				answer.append(i)
				go()
				answer.pop()

	go()

solution()
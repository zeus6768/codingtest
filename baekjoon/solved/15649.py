def main():

	def permutation(length):
		if length == M:
			print(*answer)
			return
		for i in range(1, N+1):
			if i not in answer:
				answer.append(i)
				permutation(length+1)
				answer.pop()
	
	N, M = map(int, input().split())

	answer = []
	permutation(0)

main()
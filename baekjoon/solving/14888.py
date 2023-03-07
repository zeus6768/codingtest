def main():

	def operate(i, count, result):
		if i == 0:
			result += A[count]
		elif i == 1:
			result -= A[count]
		elif i == 2:
			result *= A[count]
		else:	
			if result < 0:
				result = -((-result) // A[count])
			else:
				result //= A[count]
		return result

	def run(count, result):
		if count == N:
			answer_max[0] = max(answer_max[0], result)
			answer_min[0] = min(answer_min[0], result)
			return
		for i in range(4):
			if op[i]:
				op[i] -= 1
				run(count+1, operate(i, count, result))
				op[i] += 1
		return
	
	N = int(input())
	A = list(map(int, input().split()))
	op = list(map(int, input().split()))

	answer_max, answer_min = [-10**9], [float('inf')]
	
	run(1, A[0])
	print(f"{answer_max[0]}\n{answer_min[0]}")


main()
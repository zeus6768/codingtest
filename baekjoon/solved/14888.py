def run(count, result):
	global answer_max, answer_min
	if count == N:
		answer_max = max(answer_max, result)
		answer_min = min(answer_min, result)
		return
	for i in range(4):
		if op[i]:
			op[i] -= 1
			run(count+1, operate(i, count, result))
			op[i] += 1
	return

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

if __name__ == "__main__":
	N = int(input())
	A = list(map(int, input().split()))
	op = list(map(int, input().split()))

	answer_max, answer_min = -float('inf'), float('inf')
	
	run(1, A[0])
	print(f"{answer_max}\n{answer_min}")
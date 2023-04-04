def solve():
	size = len(nums)
	for i in range(1, size-1):
		for j in range(i+1, size):
			i, j
			
	return

if __name__ == "__main__":
	operation = input()
	nums = list()
	operands = list()
	tmp = str()
	for op in operation:
		if op.isdigit():
			tmp += op
		else:
			operands.append(op)
			nums.append(tmp)
			tmp = str()
	nums.append(tmp)
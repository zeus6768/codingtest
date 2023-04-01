def solve():
	answer = max(case_1(), case_2(), case_3())
	print(answer)

def case_1():
	# 벌집 N-1 고정, 왼쪽 벌 0 고정, 오른쪽 벌 이동
	result, r = 0, 1
	while r < N:
		left = csum_1[-1]-csum_1[0]-honey[r]
		right = csum_1[-1]-csum_1[r]
		result = max(result, left+right)
		r += 1
	return result

def case_2():
	# 벌집 이동, 왼쪽 벌 고정, 오른쪽 벌 고정
	result, hive = 0, 1
	while hive<N-1:
		left = csum_1[hive]-csum_1[0]
		right = csum_2[hive]-csum_2[-1]
		result = max(result, left+right)
		hive += 1
	return result

def case_3():
	# 벌집 0 고정, 오른쪽 벌 N-1 고정, 왼쪽 벌 이동
	result, l = 0, N-2
	while l > 0:
		left = csum_2[0]-csum_2[l]
		right = csum_2[0]-csum_2[-1]-honey[l]
		result = max(result, left+right)
		l -= 1
	return result

if __name__ == "__main__":
	N = int(input())
	honey = list(map(int, input().split()))
	csum_1, csum_2 = [honey[0]], [sum(honey)]
	for i in range(N-1):
		csum_1.append(csum_1[-1]+honey[i+1])
		csum_2.append(csum_2[-1]-honey[i])
	solve()
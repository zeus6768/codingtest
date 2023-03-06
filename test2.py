import time
from functools import reduce

def solution(e, starts):
	
	answer = [0] * len(starts)

	common_divisors = count_common_divisor(e)

	print(common_divisors)

	for idx, s in enumerate(starts):
		_max = 0
		for i in range(s, e+1):
			if _max < common_divisors[i]:
				_max = common_divisors[i]
				answer[idx] = i

	return answer


def count_common_divisor(number):
	divisor = [0] * (number+1)
	for i in range(2,number+1):
		for j in range(1,min(number//i+1,i)):
			divisor[i*j] += 2
	for i in range(1,int(number**(1/2))+1):
		divisor[i**2] += 1
	return divisor


r = solution(8, [7, 3, 1, 3])
r1 = solution(8, [1, 3, 7])
print(r)
print(r1)
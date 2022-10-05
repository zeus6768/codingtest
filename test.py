import math

def bubble_sort(array):
	result, size = array, len(array)
	for i in range(size-1):
		for j in range(size-i-1):
			if result[j+1] < result[j]:
				result[j], result[j+1] = result[j+1], result[j]
	return result

def insert_sort(array):
	result, size = [], len(array)
	for i in range(size):
		result.append(array[i])
		for j in range(i, 0, -1):
			if result[j] < result[j-1]:
				result[j-1], result[j] = result[j], result[j-1]
			else:
				break
	return result

def merge_sort(array):
	size = len(array)
	if size==1:
		return array
	
	def merge(A, B):
		if not A:
			return B
		elif not B:
			return A
		elif A[0] < B[0]:
			return [A[0]] + merge(A[1:], B)
		else:
			return [B[0]] + merge(B[1:], A)

	return merge(merge_sort(array[size//2:]), merge_sort(array[:size//2]))


def radixsort(L):
	temp = list(L)
	bucket = [[] for _ in range(10)]
	for x in range(int(math.log(max(L), 10))+1):
		bucket = [[] for _ in range(10)]
		for l in temp:
			digit = (l % 10**(x+1) // 10**x)
			bucket[digit].append(l)
			temp = []
			for i in range(len(bucket)):
				temp = temp + bucket[i]
				bucket[i] = []
	return temp

def selectk(L, k):
	if (len(L) == 1):
		return L[0]
		
	pivot = L[0]
	left = []
	right = []
	for x in L[1:]:
		if (x < pivot):
			left.append(x)
		else:
			right.append(x)
	if (len(left) == k-1):
		return pivot
	elif (len(left) >= k):
		return selectk(left, k)
	else:
		return selectk(right, k-(len(left)+1))

array = [5, 4, 3, 2, 1]
result = selectk(array, 5)
print(result)

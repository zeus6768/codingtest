def solve():
	N, K = map(int, input().split())
	A = [*map(int, input().split())]
	tmp = [0] * len(A)

	answer = [0]

	def merge_sort(array, p, r):
		if p < r:
			q = (p+r)//2
			merge_sort(array, p, q)
			merge_sort(array, q+1, r)
			merge(array, p, q, r)

	def merge(array, p, q, r):
		i, j, t = p, q+1, 0

		while i <= q and j <= r:
			if array[i] <= array[j]:
				tmp[t] = array[i]
				t += 1
				i += 1
			else:
				tmp[t] = array[j]
				t += 1
				j += 1
		
		while i <= q:
			tmp[t] = array[i]
			t += 1
			i += 1
		
		while j <= r:
			tmp[t] = A[j]
			t += 1
			j += 1
		
		i, t = p, 0

		while i <= r:
			answer[0] += 1
			if answer[0]==K:
				print(tmp[t])
				exit()
			array[i] = tmp[t]
			i += 1
			t += 1


	merge_sort(A, 0, N-1)

	print(-1)

solve()
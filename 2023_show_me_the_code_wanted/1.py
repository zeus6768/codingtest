def mine():
	N = int(input())
	statue = list(map(int, input().split()))

	answer = 1

	save_count = [0] * N
	prev = statue[0]
	count = 0

	left, right = 0, 0

	for i in range(1, N):
		if prev == statue[i]:
			if count:
				count += 1
			else:
				count = 2
			save_count[i-1] = 0
			save_count[i] = count
		else:
			count = 0
		prev = statue[i]

	print(save_count)

	for i in range(N):
		if save_count[i]:
			if statue[i] == 1:
				left += save_count[i]
				# left = max(left, save_count[i])
			else:
				right += save_count[i]
				# right = max(right, save_count[i])

	answer = max(answer, abs(left-right))

	print(answer)

def theirs():

	N=int(input())
	L=list(map(int,input().split()))

	#prefix sum
	prefix=[0 for _ in range(N)]

	for i in range(N):
		if L[i]==1:
			prefix[i]=prefix[i-1]+1

		else:
			prefix[i]=prefix[i-1]-1
	
	print(prefix)
	print(max(prefix)-min(prefix))

theirs()
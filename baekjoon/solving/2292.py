def main():

	H, W = map(int, input().split())
	blocks = list(map(int, input().split()))

	answer = 0
	filling = False
	is_fiiled = [False] * W
	max_height = blocks[0]

	for i in range(1, W-1):
		
		if blocks[i] < max_height:
			is_fiiled[i] = True

		if blocks[i] > max_height:
			max_height = blocks[i]

	ranges = []
	for i in range(W):

		if is_fiiled[i]:
			...

		
		

"""
- 두 수 사이에 두 수보다 작은 수가 있으면 비가 쌓인다

3 1 2 3 4 1 1 2
0 1 1 0 0 1 1 1

"""

		

main()


'''
      0
0     0
0     0
0   0 0

'''
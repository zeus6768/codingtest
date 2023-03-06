def main():

	def sub_sequence(now):

		if seq and sum(seq) == S:
			answer[0] += 1

		for i in range(now, N):
			seq.append(nums[i])
			sub_sequence(i+1)
			seq.pop()


	N, S = map(int, input().split())
	nums = list(map(int, input().split()))

	answer = [0]
	seq = []

	sub_sequence(0)

	print(*answer)

main()

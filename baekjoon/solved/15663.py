def get_sequence():
	if len(seq)==M:
		s = [str(nums[i]) for i in seq]
		s = " ".join(s)
		if s not in results:
			results.add(s)
			print(s)
		return
	for i in range(N):
		if i not in seq:
			seq.append(i)
			get_sequence()
			seq.pop()
	return

if __name__ == "__main__":
	N, M = map(int, input().split())
	nums = sorted(map(int, input().split()))
	seq = list()
	results = set()
	get_sequence()
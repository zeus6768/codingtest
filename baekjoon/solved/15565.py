def solve():

	if K == 1:
		print(1) if 1 in dolls else print(-1)
		return
	
	answer = float('inf')

	csum = [int(dolls[0]==1)]
	[csum.append(csum[-1]+int(dolls[i]==1)) for i in range(1, N)]

	l, r = 0, 1
	while l <= r < N:
		if dolls[l]==dolls[r]==1 and csum[r]-csum[l]==K-1:
			answer = min(answer, r-l+1)
			l += 1
		elif dolls[r] != 1 or dolls[l]==dolls[r]==1 and csum[r]-csum[l]<K-1:
			r += 1
		elif dolls[l] != 1 or dolls[l]==dolls[r]==1 and csum[r]-csum[l]>K-1:
			l += 1
	
	print(answer) if answer != float('inf') else print(-1)

if __name__ == "__main__":
	N, K = map(int, input().split())
	dolls = tuple(map(int, input().split()))
	solve()
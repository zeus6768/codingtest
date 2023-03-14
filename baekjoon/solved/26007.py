def input():
	return __import__('sys').stdin.readline()

def main():
	ratings = [X]
	for i in range(N):
		ratings.append(ratings[-1] + A[i])

	compares = [ratings[i]<K for i in range(N+1)]
	
	csum = [0]
	for i in range(N+1):
		csum.append(csum[-1]+compares[i])

	for _ in range(M):
		l, r = map(int, input().split())
		answer = csum[r] - csum[l]
		print(answer)

N, M, K, X = map(int, input().split())
A = list(map(int, input().split()))

main()
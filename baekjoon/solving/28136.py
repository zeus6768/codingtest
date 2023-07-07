N = int(input())
A = tuple(map(int, input().split()))

answer = 0
for i in range(N-1):
	if A[i] >= A[i+1]:
		answer += 1

if A[0] <= A[N-1]:
	answer += 1

print(answer)
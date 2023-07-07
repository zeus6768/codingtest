N = int(input())
A = tuple(map(int, input().split()))

answer = 0
for i in range(20):
	count = sum(bool(a & (2 ** i)) for a in A)
	answer = max(answer, count)

print(answer)
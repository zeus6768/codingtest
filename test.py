# n장 중 2장 골라 m에 가장 가까운 값 구하기
n, m = map(int, input().split())
arr = [*map(int, input().split())]
ans = 0

for i in range(n):
	for j in range(i+1, n):
		sum_card = arr[i] + arr[j]
		if abs(sum_card - m) < abs(ans - m):
			ans = sum_card

print(ans)

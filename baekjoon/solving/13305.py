N = int(input())
roads = tuple(map(int, input().split()))
prices = tuple(map(int, input().split()))

answer = 0
price = prices[0]
for i in range(N-1):
	if prices[i] < price:
		price = prices[i]
	answer += price * roads[i]

print(answer)
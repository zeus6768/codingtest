def match_to_number(num):
	
	for cost in costs:
		for c in range(cost, num+1):
			dp[c] = [min(dp[c], dp[c-cost]+dp[cost]), max()]
	
	return

def main():

	for _ in range(int(input())):
		n = int(input())
		match_to_number(n)

	return

costs = (2, 3, 4, 5, 6, 7)

cost_to_number = (
	(),
	(),
	(1),
	(7),
	(4),
	(2, 3, 5),
	(0, 6, 9),
	(8)
)

dp = [[0, 0] for _ in range(101)]

main()
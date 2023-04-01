def solve(X):
	while X:
		if X % 3 == 0:
			if dp[X]+1 < dp[X//3]:
				dp[X//3] = dp[X]+1
				graph[X//3] = X
		if X % 2 == 0:
			if dp[X]+1 < dp[X//2]:
				dp[X//2] = dp[X]+1
				graph[X//2] = X
		if dp[X]+1 < dp[X-1]:
			dp[X-1] = dp[X]+1
			graph[X-1] = X
		X -= 1
	print(dp[1])
	print(*search())

def search():
	result = list()
	stack = [1]
	while stack:
		node = stack.pop()
		result.append(node)
		if graph[node]:
			stack.append(graph[node])
	return result[::-1]

if __name__ == "__main__":
	X = int(input())
	dp = [float('inf')] * (X+1)
	dp[X] = 0
	graph = [0] * (X+1)
	solve(X)
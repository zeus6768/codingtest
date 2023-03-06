import sys
input = sys.stdin.readline

def main():

	def strahler(node):

		if not graph[node]:
			return 1
		
		if orders[node] != 1:
			return orders[node]
		
		count, order_max = 0, 0
		for n in graph[node]:
			order = strahler(n)
			if order_max == order:
				count += 1
			if order_max < order:
				count = 1
				order_max = order
			# print(f"node={node}, orders[node]={orders[node]}, upstream={n}, order={order}, order_max={order_max}")

		if count >= 2:
			orders[node] = order_max + 1
		else:
			orders[node] = order_max

		return orders[node]
	
	T = int(input())
	
	for _ in range(T):
		
		K, M, P = map(int, input().split())
		
		graph = [[] for _ in range(M+1)]
		orders = [1] * (M+1)
		for _ in range(P):
			A, B = map(int, input().split())
			graph[B].append(A)

		[strahler(i) for i in range(1, M+1)]

		print(K, orders[M])

main()
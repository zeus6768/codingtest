from sys import stdin
input = stdin.readline

def solve():

	M_MAX, P_MAX = 1000, 500
	
	dp = [[-1] * (M_MAX+2) for _ in range(P_MAX+1)]
	dp[0][0] = 0
	
	answer = -1

	N, M, K = map(int, input().split())
	
	cpu, memory, priority = [0], [0], [0]
	for _ in range(N):
		c, m, p = map(int, input().split())
		cpu.append(c)
		memory.append(m)
		priority.append(p)

	for i in range(N):
		for j in range(P_MAX, -1, -1):
			for k in range(M_MAX, -1, -1):
				if j + priority[i] > P_MAX:
					continue
				if k + cpu[i] <= M_MAX:
					dp[j+priority[i]][k+cpu[i]] = max(dp[j+priority[i]][k+cpu[i]], dp[j][k] + memory[i])
				if k + cpu[i] > M_MAX:
					dp[j+priority[i]][M_MAX+1] = max(dp[j+priority[i]][M_MAX+1], dp[j][k] + memory[i])

	for i in range(P_MAX+1):
		for j in range(M, M_MAX+2):
			if dp[i][j] >= K and (answer == -1 or answer > i):
				answer = i

	print(answer)

solve()


def main():
	now = (0, 0)
	dfs(0, now, 1)
	print(answer)
	return

def dfs(depth, now_xy, prob):
	global answer
	if depth == N:
		answer += prob
		return
	for i in range(4):
		next_xy = (now_xy[0]+EWSN[i][0], now_xy[1]+EWSN[i][1])
		if visited[next_xy[0]][next_xy[1]]:
			continue
		next_prob = prob * probs[i]
		visited[next_xy[0]][next_xy[1]] = True
		dfs(depth+1, next_xy, next_prob)
		visited[next_xy[0]][next_xy[1]] = False
	return

N, EP, WP, SP, NP = map(int, input().split())

visited = [[False] * (N*2+1) for _ in range(N*2+1)]
visited[0][0] = True

probs = tuple(map(lambda x: x/100, (EP, WP, SP, NP)))
EWSN = ((0, 1), (0, -1), (1, 0), (-1, 0))

answer = 0

main()
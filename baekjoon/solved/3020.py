import sys

def input():
	return sys.stdin.readline()

def solve():
	c_stalagmites = [N//2]
	for i in range(H):
		c_stalagmites.append(c_stalagmites[-1]-stalagmites[i])

	c_stalactites = [0]
	for i in range(H,0,-1):
		c_stalactites.append(c_stalactites[-1]+stalactites[i])

	answer, count = float("inf"), 0
	for i in range(1, H+1):
		total = c_stalagmites[i] + c_stalactites[i]
		if total == answer:
			count += 1
		elif total < answer:
			answer = total
			count = 1

	print(answer, count)

if __name__ == "__main__":
	N, H = map(int, input().split())

	stalagmites, stalactites = [0]*(H+1), [0]*(H+1)

	for i in range(N):
		length = int(input())
		if i%2==0:
			stalagmites[length] += 1
		else:
			stalactites[length] += 1

	solve()
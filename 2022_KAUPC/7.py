import sys
input = sys.stdin.readline

def solve():

	n, m, q = map(int, input().split())
	A = [*map(int, input().split())]

	answer = 0

	for _ in range(q):
		t1, t2 = map(int, input().split())

		if t1 == 1:
			for i in range(t2):
				v = A[i] - m*(t2-1-i)
				if v < 0:
					v = 0
				answer += v
		else:
			day5 = []

			for i in range(t2-1):
				v = A[i] - m*(t2-2-i)
				if v < 0:
					day5.append(0)
				else:
					day5.append(v)

			for d in day5:
				if d < m:
					answer += d
				else:
					answer += m
	
		print(answer)

	return


solve()
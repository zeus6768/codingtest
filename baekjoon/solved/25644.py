def main():
	MIN, ANSWER = 10**9, 0
	for a in A:
		MIN = min(MIN, a)
		ANSWER = max(ANSWER, a-MIN)
	print(ANSWER)

N = int(input())
A = tuple(map(int, input().split()))

main()
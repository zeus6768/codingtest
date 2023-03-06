def main():
	input()
	A = sorted(map(int, input().split()))
	B = sorted(map(int, input().split()), reverse=True)
	S = sum([a*b for a, b in zip(A, B)])
	print(S)

main()
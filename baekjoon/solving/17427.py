def main():
	N = int(input())
	answer = sum(i*(N//i) for i in range(1, N+1))
	print(answer)
main()
def main():
	A, B, C = map(int, input().split())
	X, Y, Z = map(int, input().split())

	answer = 0
	
	for _ in range(3):
		chicken, pizza, burger = min(A, X), min(B, Y), min(C, Z)
		answer += chicken + pizza + burger
		A -= chicken
		X -= chicken
		B -= pizza
		Y -= pizza
		C -= burger
		Z -= burger
		X, Y, Z = Z//3, X//3, Y//3

	print(answer)

main()
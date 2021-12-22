def solution():
	answer = []
	while True:
		a, b, c = map(int, input().split())
		if a == b == c == 0:
			break
		else:
			answer.append(is_right_angle(a, b, c))
	[print(a) for a in answer]

def is_right_angle(x, y, z):
	if (x**2 == y**2+z**2) or (y**2 == x**2+z**2) or (z**2 == x**2+y**2):
		return "right"
	else:
		return "wrong"

solution()
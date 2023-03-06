from sys import stdin

def input():
	return stdin.readline()

# a*b - c*d
def main():
	K = int(input())
	# field = [tuple(map(int, input().split())) for _ in range(6)]

	ab = []
	field = []
	direction_count = [0] * 5
	a, b, c, d = [[0, 0] for _ in range(4)]

	for i in range(6):
		direction, length = map(int, input().split())
		direction_count[direction] += 1
		field.append((direction, length))

	[ab.append(i) for i in range(1, 5) if direction_count[i]==1]

	print(ab)
	print(field)

	return

main()
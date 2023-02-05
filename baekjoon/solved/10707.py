def calculate_y(usage):
	if P <= C:
		return B
	return B + (usage - C) * D
	
A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

X = A * P
Y = calculate_y(P)

print(min(X, Y))
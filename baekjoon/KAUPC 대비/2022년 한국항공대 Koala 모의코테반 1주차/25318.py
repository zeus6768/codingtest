from datetime import datetime
import sys
input = sys.stdin.readline

def get_t(dt):
	dt = datetime.strptime(dt, "%Y/%m/%d %H:%M:%S")
	default = datetime(2019, 6, 6, 0, 0, 0)
	default.d
	result = dt - default
	return result.days + result.seconds/60/60/24
	
def get_p(T, n):
	P = [0]
	[P.append(max(0.5**((T[n]-T[i])/365), 0.9**(n-i))) for i in range(1, n+1)]
	return P

def get_x(P, L):
	a, b = 0, 0
	for p, l in zip(P, L):
		a += p*l
		b += p
	return round(a / b)

def solve():
	n = int(input())
	if n == 0: 
		print(0)
		return

	T, L= [0], [0]

	for _ in range(n):
		*dt, level = input().split()
		dt = " ".join(dt)
		T.append(get_t(dt))
		L.append(int(level))

	P = get_p(T, n)
	X = get_x(P, L)

	print(X)

solve()


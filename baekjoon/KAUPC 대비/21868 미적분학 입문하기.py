from fractions import Fraction as F

e1, e2 = map(int, input().split())
e = F(e1, e2)
a, c = map(int, input().split())
x = int(input())

if a == 0:
	L = c
	max_d = (0, 0)
else:
	L = a * x + c
	max_d = max(F((e-(a*x)-c+L)/a), F((-e-(a*x)-c+L)/a))
	max_d = (max_d.numerator, max_d.denominator)

print(L)
print(max_d[0], max_d[1])
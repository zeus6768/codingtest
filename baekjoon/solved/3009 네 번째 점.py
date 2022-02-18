points = [tuple(map(int, input().split())) for _ in range(3)]
x, y = {}, {}
for p in points:
	if p[0] in x:
		x[p[0]] += 1
	else:
		x[p[0]] = 1
	if p[1] in y:
		y[p[1]] += 1
	else:
		y[p[1]] = 1

def find(xs, ys):
	x, y = 0, 0
	for a in xs:
		if xs[a] == 1:
			x = a
	for b in ys:
		if ys[b] == 1:
			y = b
	return x, y

result = find(x, y)
print(result[0], result[1])
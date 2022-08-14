n = int(input())

l, r = 1, n

while l <= r:
	m = int((l+r)//2)

	if m**2 == n:
		print(m)
		break
	elif m**2 < n:
		l = m + 1
	else:
		r = m - 1
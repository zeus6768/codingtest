h, m = map(int, input().split())
t = int(input())

def timer(h, m, t):
	time = h * 60 + m + t
	if time >= 1440: time %= 1440
	return f"{time//60} {time%60}"

print(timer(h, m, t))
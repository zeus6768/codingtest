h, m = map(int, input().split())
time = h * 60 + m - 45
if time >= 0:
    h, m = time // 60, time % 60
else:
    time = 1440 + time
    h, m = time // 60, time % 60
print(h, m)
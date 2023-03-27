w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
qx, rx = (t - (w - p)) // w, (t - (w - p)) % w
qy, ry = (t - (h - q)) // h, (t - (h - q)) % h
x = rx if qx%2 else w-rx
y = ry if qy%2 else h-ry
print(x, y)
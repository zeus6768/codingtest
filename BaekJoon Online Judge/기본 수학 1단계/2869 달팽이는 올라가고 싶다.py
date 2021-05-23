a, b, v = map(int, input().split())
q = (v - a) // (a - b)
if (a - b) * q == v - a:
    print(q + 1)
else:
    print(q + 2)
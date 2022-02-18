def GCD(n, m):
    while m:
        n, m = m, n % m
    return n

def LCM(n, m):
    return

print(GCD(3, 12))
print(LCM(3, 12))
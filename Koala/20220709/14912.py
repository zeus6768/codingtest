n, d = input().split()
print(sum([str(i).count(d) for i in range(1, int(n)+1)]))
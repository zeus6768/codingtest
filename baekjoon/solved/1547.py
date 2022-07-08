cups = [1, 0, 0]
for _ in range(int(input())):
	x, y = map(lambda x: int(x)-1, input().split())
	cups[x], cups[y] = cups[y], cups[x]
print(cups.index(1)+1)

# [1, 2, 3]
# 3 1 => [3, 2, 1]
# 2 3 => [2, 3, 1]
# 3 1 => [2, 1, 3]
# 3 2 => [3, 1, 2]
table = [[*map(int, input().split())] for _ in range(9)]
blank = [(i, j) for j in range(9) for i in range(9) if table[i][j]==0]

print(blank)
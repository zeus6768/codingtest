h, w, n, l, d, x, y = [0] * 7
board = []
arr = []

# 입력
h, w = map(int, input().split())
n = int(input())
for _ in range(n):
    l, d, x, y = map(int, input().split())
    arr.append((l, d, x - 1, y - 1))

# 격자판 생성
for i in range(h):
    board.append([0] * w)

# 막대 놓기
for k in range(n):
    dy = arr[k][2]
    dx = arr[k][3]
    for j in range(arr[k][0]):
        # 가로 막대
        if arr[k][1] == 0:
            board[dy][dx + j] = 1
        # 세로 막대
        else:
            board[dy + j][dx] = 1

# 출력
for o in range(h):
    for p in range(w):
        print(board[o][p], end = ' ')
    print()
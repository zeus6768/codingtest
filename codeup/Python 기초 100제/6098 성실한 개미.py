# 미로 생성
maze = []
for i in range(10):
    input_maze = list(map(int, input().split()))
    maze.append(input_maze)

# 개미 생성
class Ant():
    def __init__(self):
        self.x = 1
        self.y = 1
        self.value = 0

# 초기화
ant = Ant()
maze[ant.y][ant.x] = 9

# 실행
while ant.value != 2:
    # 오른쪽 경로 확인
    if maze[ant.y][ant.x + 1] == 1:
        # 아래 경로 확인
        if maze[ant.y + 1][ant.x] == 1:
            break
        else:
            ant.y += 1
            ant.value = maze[ant.y][ant.x]
    else:
        ant.x += 1
        ant.value = maze[ant.y][ant.x]

    # 방문한 위치 9 입력
    maze[ant.y][ant.x] = 9

# 출력
for k in range(10):
    for l in range(10):
        print(maze[k][l], end = ' ')
    print()
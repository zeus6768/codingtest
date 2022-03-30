from sys import stdin
input = stdin.readline

def solution(m, num):
    global answer
    
    if num > 1:
        result = sum([abs(rgb[i]//num - gom[i]) for i in range(3)])
        answer = min(answer, result)

    for i in range(m+1, n):
        rgb[0] += arr[i][0]
        rgb[1] += arr[i][1]
        rgb[2] += arr[i][2]
        solution(i, num+1) if num < 7 else None
        rgb[0] -= arr[i][0]
        rgb[1] -= arr[i][1]
        rgb[2] -= arr[i][2]

n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]
gom = [*map(int, input().split())]
rgb = [0, 0, 0]
answer = float('inf')

solution(-1, 0)
print(answer)
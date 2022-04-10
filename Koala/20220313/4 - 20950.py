input = __import__('sys').stdin.readline

def main():
    n = int(input())
    arr = [[*map(int, input().split())] for _ in range(n)]
    gom = [*map(int, input().split())]
    rgb = [0, 0, 0]
    answer = [float('inf')]

    def solution(m, num):
        if num > 1:
            result = sum([abs(rgb[i]//num - gom[i]) for i in range(3)])
            answer[0] = min(answer[0], result)

        for i in range(m+1, n):
            rgb[0] += arr[i][0]
            rgb[1] += arr[i][1]
            rgb[2] += arr[i][2]
            solution(i, num+1) if num < 7 else None
            rgb[0] -= arr[i][0]
            rgb[1] -= arr[i][1]
            rgb[2] -= arr[i][2]

    solution(-1, 0)
    print(*answer)

main()

# correct
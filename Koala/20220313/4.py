from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    arr = [[*map(int, input().split())] for _ in range(n)]
    gom = [*map(int, input().split())]

    rgb = [0, 0, 0]
    for i in range(n):
        rgb[0] += arr[i][0]
        rgb[1] += arr[i][1]
        rgb[2] += arr[i][2]
    rgb = [*map(lambda x: x//n, rgb)]

    result = 0
    for a, b in zip(gom, rgb):
        result += abs(a-b)
    
    print(result)

main()
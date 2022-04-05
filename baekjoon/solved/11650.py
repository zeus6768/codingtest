input = __import__('sys').stdin.readline
[print(*a) for a in sorted([[*map(int, input().split())] for _ in range(int(input()))])]

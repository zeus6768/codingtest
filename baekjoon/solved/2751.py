input = lambda: int(__import__('sys').stdin.readline())
[print(n) for n in sorted([input() for _ in range(input())])]
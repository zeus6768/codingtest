input = __import__('sys').stdin.readline
[print(w) for w in sorted([*set([input().strip() for _ in range(int(input()))])], key=lambda w: (len(w), w))]

from sys import stdin
input = stdin.readline

def main():
    s = input().strip()
    n = int(input())
    rings = [input().strip() for _ in range(n)]
    rings = [*map(lambda x: x*2, rings)]

    result = 0
    for r in rings:
        if s in r:
            result += 1

    print(result)

main()

# correct

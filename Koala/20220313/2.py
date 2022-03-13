from sys import stdin
input = stdin.readline

def main():
    x = input().rstrip()
    cal = 0

    while len(x) > 1:
        x = str(sum(map(int, x)))
        cal += 1
        print(x, cal)

    print(cal)
    if int(x) % 3:
        print("NO")
    else:
        print("YES")

main()
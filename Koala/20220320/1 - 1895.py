
def main():
    r, c = map(int, input().split())
    pic = [[*map(int, input().split())] for _ in range(r)]
    T = int(input())

    J = []
    for i in range(1, r-1):
        for j in range(1, c-1):
            tmp = pic[i-1][j-1:j+2] + pic[i][j-1:j+2] + pic[i+1][j-1:j+2]
            J.append(mid_value(tmp))

    answer = 0
    for k in J:
        answer += 1 if k >= T else 0

    print(answer)

def mid_value(arr):
    return sorted(arr)[4]

main()

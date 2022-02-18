t = int(input())
cases = [[int(input()) for i in range(2)] for j in range(t)]


def flat(k, n):
    save = [[0] * n for _ in range(k + 1)]
    if save[k][n - 1]:
        return save[k][n - 1]
    elif k == 0 or n == 1:
        save[k][n - 1] = n
        return n
    else:
        save[k][n - 1] = flat(k - 1, n) + flat(k, n - 1)
        return save[k][n - 1]

[print(flat(case[0], case[1])) for case in cases]
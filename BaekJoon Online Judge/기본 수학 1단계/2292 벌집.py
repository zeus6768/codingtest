# https://www.acmicpc.net/problem/2292
import math
number = int(input())
def quadratic(x):   # 근의공식으로 x가 어떤 n과 가까운지 근사
    if x == 1 : return 1
    a = 3; b = -9; c = 8 - x    # 일반항 (3n**2 - 9*n + 8)의 계수
    return (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
print(int(quadratic(number)))
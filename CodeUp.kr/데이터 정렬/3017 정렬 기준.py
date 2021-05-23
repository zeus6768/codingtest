from operator import itemgetter
n = int(input()); score_arr = []
for i in range(n):
    math, info = map(int, input().split())
    score_arr.append([i + 1, math, info])
new_arr = sorted(score_arr, key = itemgetter(1, 2), reverse = True)
[print(new_arr[index][0], new_arr[index][1], new_arr[index][2]) for index in range(n)]
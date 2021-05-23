from operator import itemgetter
n = int(input()); arr = []
for i in range(n):
    title, year, month, day = input().split()
    arr.append([title, int(year), int(month), int(day)])
new_arr = sorted(arr, key = itemgetter(1, 2, 3, 0))
[print(new_arr[j][0]) for j in range(n)]
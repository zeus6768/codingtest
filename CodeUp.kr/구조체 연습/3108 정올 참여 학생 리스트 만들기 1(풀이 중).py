from operator import itemgetter
n = int(input()); arr = []
for i in range(n):
    code, num, name = input().split()
    arr.append([code, int(num), name])
#arr.sort(key = itemgetter(1))
print(arr)
result_arr = []
for j in arr:
    if j[0] == 'I':
        result_arr.append([j[1], j[2]])
    elif j[0] == 'D':
        
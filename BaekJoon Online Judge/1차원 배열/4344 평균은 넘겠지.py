c = int(input())
list1 = [input() for _ in range(c)]

for i in range(len(list1)):
    list1[i] = list(map(int, list1[i].split()))

def percentage(arr):
    n = arr[0]
    average = sum(arr[1:]) / n
    arr = arr[1:]
    for j in range(len(arr)):
        if arr[j] > average:
            arr[j] = 1
        else: 
            arr[j] = 0
    result = sum(arr) / n * 100
    return round(result, 3)

[print("%.3f%%" % percentage(k)) for k in list1]
    
'''입력
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91
'''
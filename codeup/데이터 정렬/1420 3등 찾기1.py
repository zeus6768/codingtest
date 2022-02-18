arr = []
dic1 = {}

n = int(input())
for i in range(n):
    value, key = input().split()
    dic1[int(key)] = value
    arr.append(int(key))

arr.sort(reverse = True)
print(dic1[arr[2]])
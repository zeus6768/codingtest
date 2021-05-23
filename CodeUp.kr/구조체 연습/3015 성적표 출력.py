from operator import itemgetter

n, m = map(int, input().split())
array = [input().split() for i in range(n)]

for num in array:
  num[1] = int(num[1])
print(array)

new_array = sorted(array, key = itemgetter(1), reverse = True)
print(new_array)

for arr in range(m):
  print(new_array[arr][0])
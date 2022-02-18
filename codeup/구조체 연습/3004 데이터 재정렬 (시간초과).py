import sys 

n = int(input())
array = sys.stdin.readline().rstrip().split()
array = list(map(int, array))
sorted_array = sorted(array)

for num in array:
  index_of_num = sorted_array.index(num)
  print(index_of_num, end = ' ')    
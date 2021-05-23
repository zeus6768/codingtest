from sys import stdin

n, m = map(int, stdin.readline().split())
array1 = [tuple(stdin.readline().rstrip().split()) for _ in range(n)]
array2 = [stdin.readline().rstrip() for _ in range(m)]

result_dic = {}
for name in array2:
    result_dic[name] = 0

for tup1 in array1:
    if tup1[0] in result_dic:
        result_dic[tup1[0]] += int(tup1[1])

for name in array2:
    print(result_dic[name])
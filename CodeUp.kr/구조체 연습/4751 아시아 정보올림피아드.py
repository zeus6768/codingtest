from sys import stdin
from operator import itemgetter
n = int(stdin.readline().rstrip())
input_table = [tuple(map(int, stdin.readline().rstrip().split())) for _ in range(n)]
ranked_table = sorted(input_table, key = itemgetter(2), reverse = True)
result_table = []
for i in range(3):
    if i == 2 and (result_table[0][0] != result_table[1][0]):
        result_table.append(ranked_table[i])
    elif i == 2 and (result_table[0][0] == result_table[1][0]):
        for tup1 in ranked_table:
            if tup1[0] != result_table[0][0]:
                result_table.append(tup1)
                break
    else:
        result_table.append(ranked_table[i])
[print(j[0], j[1]) for j in result_table]
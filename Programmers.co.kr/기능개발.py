# 나의 풀이
from os import remove


def solution(progresses, speeds):
    from collections import deque
    answer = []
    days_left = []
    cnt = 0
    for p, s in zip(progresses, speeds):
        days_left.append((100 - p) / s)
        # [7, 2.333, 9]
    for n in days_left:
        tmp = []
        for i in range(len(days_left)):
            if n >= days_left[i]:
                tmp.append(days_left[i])
        days_left.remove(days_left[i])
        answer.append(len(tmp))

    return answer

print(solution([93, 30, 55], [1, 30, 5]))

# 다른 사람의 풀이

#[93, 30, 55]	[1, 30, 5]	[2, 1]
#[95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]
# 나의 풀이
def solution1(priorities, location):
    answer_num = priorities[location]
    Q = [[priorities[i], i] for i in range(len(priorities))]
    for i in range(len(priorities)):
        if priorities[i] != max(priorities[i:]):
            priorities[i], priorities[-1] = max(priorities[i:]), priorities[i]
            
    answer = priorities.index(answer_num) + 1
    return answer

priorities = [1, 1, 9, 1, 1, 1]
Q = [[priorities[i], i] for i in range(len(priorities))]
print(Q)

# 입력, 결과
# [2, 1, 3, 2]	2	1
# [1, 1, 9, 1, 1, 1]	0	5
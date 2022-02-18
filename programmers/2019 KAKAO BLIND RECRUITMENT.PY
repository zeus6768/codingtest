from collections import Counter

def solution(N, stages):
    answer = []
    user_num = len(stages)
    counter = Counter(stages)
    for c in range(1, N+1):
        user_num -= counter[c-1]
        answer.append([c, counter[c]/user_num]) if user_num else answer.append([c, 0])
    return [a[0] for a in sorted(answer, key=lambda x: x[1], reverse=True)]

result = solution(5, [1, 1, 1, 1, 1, 1, 1, 2])
print(result)
# 나의 풀이
def solution1(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    le = len(completion)
    for i in range(le):
        if participant[i] == completion[i]:
            pass
        else:
            answer = participant[i]
            return answer
    return participant[le]

# 다른 사람의 풀이
from collections import Counter

p = ["marina", "marina", "josipa", "nikola", "vinko", "filipa"]
c = ["josipa", "filipa", "marina", "nikola"]
print(Counter(p))
print(Counter(c))

def solution2(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return answer

r = solution2(p, c)
print(list(r))
from collections import Counter

def solution(N, stages):
    answer = []
    counter = Counter(stages)
    유저수 = len(stages)
    스테이지_실패율 = {}

    for i in range(1, N+1):
        if 유저수:
            스테이지_실패율[i] = counter[i] / 유저수
            유저수 -= counter[i]
        
    for tup in sorted(스테이지_실패율.items(), key=lambda x: x[1], reverse=True):
        answer.append(tup[0])
        
    return answer
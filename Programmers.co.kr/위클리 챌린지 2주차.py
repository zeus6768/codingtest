def solution(scores):
    def grade(score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 50:
            return "D"
        else: 
            return "F"
        
    answer = ""
    score_each = {}
    length = len(scores)
    
    for i in range(length): 
        score_each[i] = []
    for s in scores:
        for j in range(length):
            score_each[j].append(s[j])
            
    for k in range(length):
        score_list = score_each[k]
        self_score = score_list[k]
        maxim = max(score_list)
        minim = min(score_list)
        is_unique = (score_list.count(self_score) == 1)
        if (is_unique) and (maxim == self_score or minim == self_score):
            score_list.remove(self_score)
        answer += grade(sum(score_list)/len(score_list))
    
    return answer


def solution2(scores):
    avgs = []
    score = [[i[j] for i in scores] for j in range(len(scores))]

    for idx, i in enumerate(score):
        avg = sum(i)
        length = len(i)
        if (i[idx] == max(i) or i[idx] == min(i)) and (i.count(i[idx]) == 1):
            avg -= i[idx]
            length -= 1
        avgs.append(avg/length)
    
    return "".join([avg>=90 and "A" or avg>=80 and "B" or avg>=70 and "C" or avg>=50 and "D" or "F" for avg in avgs])
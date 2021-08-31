def solution(s):
    answer = ""
    sl = s.split()
    for word in sl:
        for j in range(len(word)):
            if j % 2:
                answer += word[j].lower()
            else:
                answer += word[j].upper()
        answer += " "
    answer.strip()
    return answer

print(solution("try hello world"))
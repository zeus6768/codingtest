def solution(s):
    return True if (len(s) == 4 or len(s) == 6) and s.isdigit() else False


# 다른 사람의 풀이
def solution2(s):
    return s.isdigit() and len(s) in (4, 6)


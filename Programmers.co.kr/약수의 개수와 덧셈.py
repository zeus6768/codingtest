def solution(left, right):
    def 약수의개수(n):
        result = 1
        for i in range(1, n//2+1):
            if n % i == 0:
                result += 1
        return result
    answer = 0
    for m in range(left, right+1):
        if 약수의개수(m) % 2:
            answer -= m
        else:
            answer += m
    return answer

result = solution(13, 17)
print(result)
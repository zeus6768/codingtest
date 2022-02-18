def solution(n):
    answer, aliquot = 0, 1
    if n:
        while n != aliquot:
            if n % aliquot:
                aliquot += 1
            else:
                answer += aliquot        
                aliquot += 1
        return answer + aliquot
    else:
        return answer

def solution2(n):
    return n + sum([i for i in range(1, (n // 2) + 1) if n % i == 0])

def solution3(n):
    return sum(filter(lambda x: n % x == 0, range(1, n + 1)))


result = solution3(3000)
print(result)
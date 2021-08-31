import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return
        else:
            pass
    return n

def solution(n):
    answer = 0
    for i in range(2, n + 1):
        if is_prime(i):
            answer += 1
    return answer

# 에라토스테네스의 체
def solution2(n):       
    num=set(range(2,n+1))
    for i in range(2,n+1):      
        if i in num:
            num-=set(range(i*i,n+1,i))
    return len(num)

print(solution2(1000000))

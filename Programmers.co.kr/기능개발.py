# 나의 풀이
import math

def solution1(progresses, speeds):
    answer = []
    stack = []

    for i in range(len(progresses)):
        days_left = math.ceil((100 - progresses[i]) / speeds[i])

        if i == 0:
            stack.append(days_left)
        else:
            if stack[0] >= days_left:
                stack.append(days_left)
            else:
                answer.append(len(stack))
                stack.clear()
                stack.append(days_left)

    answer.append(len(stack))

    return answer


# 다른 사람의 풀이
def solution2(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]


# 입력
print(solution1([93, 30, 55], [1, 30, 5]))
print(solution2([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
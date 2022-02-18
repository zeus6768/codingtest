n = int(input())
score_list = list(map(int, input().split()))

def cheat(number):
    max_score = max(score_list)
    return number / max_score * 100

new_list = list(map(cheat, score_list))

def average(arr):
    sum = 0
    for _ in arr:
        sum += _
    return sum / len(arr)

print(average(new_list))
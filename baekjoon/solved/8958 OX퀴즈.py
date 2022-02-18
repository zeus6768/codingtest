n = int(input())
quiz_result = [input() for i in range(n)]

def summation(number):
    if number == 1:
        return 1
    else:
        return int(number * (number + 1) / 2)

def ox_to_score(arr):
    for j in range(len(arr)):
        score = 0
        arr[j] = arr[j].split('X')
        for k in arr[j]:
            score += summation(len(k))
        arr[j] = score
    return arr

result = ox_to_score(quiz_result)
[print(_) for _ in result]


'''입력
5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX
'''
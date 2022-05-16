def solution():
    n = int(input())
    score = [*map(int, input().split())]
    _max = max(score)
    score = [*map(lambda x: x/_max*100, score)]
    avg = sum(score) / n
    print(avg)
solution()
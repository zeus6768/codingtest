from itertools import permutations as pm
numbers = [1, 2, 3, 4, 5]

print(*pm(numbers))

def main():
    answers = [*map(int, input().split())]
    numbers = [1, 2, 3, 4, 5]
    young = [*pm(numbers, 10)]
    count = 0
    arr = [0] * 10



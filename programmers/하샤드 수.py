def solution(x):
    add = sum(map(int, list(str(x))))
    return False if x % add else True
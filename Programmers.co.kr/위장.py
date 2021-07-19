# 나의 풀이
def solution1(clothes):
    hash_table = dict()
    for cloth, kind in clothes:
        if kind not in hash_table:
            hash_table[kind] = 1
        else:
            hash_table[kind] += 1
            
    answer = 1
    for value in hash_table.values():
        answer *= (value + 1)
        
    answer -= 1
    return answer

# 다른 사람의 풀이
def solution2(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    print(cnt)
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer


a = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
b = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]


print(solution2(a))
print(solution2(b))
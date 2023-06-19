def find(letter):
    result = [(i, j) for i in range(len(keyboard)) for j in range(len(keyboard[0])) if keyboard[i][j]==letter]
    result.sort(key=lambda rc: sum(rc))
    return result

def get_distance(rc1, rc2):
    return abs(rc1[0]-rc2[0]) + abs(rc1[1]-rc2[1])

def get_min_distacne(list1, list2):
    min_distance = float("inf")
    for rc1 in list1:
        for rc2 in list2:
            min_distance = min(min_distance, get_distance(rc1, rc2))
    return min_distance

def solution(word):
    distance, count = 0, 0
    n = len(word)
    for i in range(n-1):
        if word[i]==word[i+1]:
            count += 1
            continue
        positions_1 = find(word[i])
        positions_2 = find(word[i+1])
        if not positions_1:
            distance += 20
            count += 1
        elif not positions_2:
            continue
        else:
            distance += get_min_distacne(positions_1, positions_2)
            count += 1
    return [distance, count]

keyboard = [
    "가호저론남드부이프설",
    "알크청울키초트을배주",
    "개캠산대단지역구너양",
    "라로권교마쿼파송차타",
    "코불레뉴 서한산리개",
    "터강봄토캠상호론운상",
    "보람이경아두프바트정",
    "스웨어쿼일소라가나도",
    "판자비우사거왕태요품",
    "안배차캐민광재봇북하"
]

location = dict()

input_1 = "부스트캠프"      # 30, 4
input_2 = "부슈트캠프"      # 35, 3
input_3 = "불레뉴캠프"      # 7, 4
input_4 = "뉴$솔레어"       # 43, 3
input_5 = "뉴뉴"            # 0, 1

for inp in (input_1, input_2, input_3, input_4, input_5):
    print(solution(inp))
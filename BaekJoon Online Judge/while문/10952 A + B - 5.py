a, b = 1, 1
answer_list = []
while a and b:
    a, b = map(int, input().split())
    answer_list.append(a + b)
[print(num) for num in answer_list[:-1]]
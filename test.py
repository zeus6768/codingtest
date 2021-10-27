list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list3 = [11, 12, 13, 14, 15]

# 리스트가 여러 개 있을 때, 같은 인덱스의 값만 모아서 새로운 리스트를 생성하는 방법
list4 = []
list4.append(list1)
list4.append(list2)
list4.append(list3)

list5 = []
list5 = [[lis[i] for lis in list4] for i in range(len(list1))]

print(list5)
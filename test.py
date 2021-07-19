list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list3 = [11, 12, 13, 14, 15]

my_function1 = lambda a, b, c : a + b + c
list4 = list(map(my_function1, list1, list2, list3))
print(list4)
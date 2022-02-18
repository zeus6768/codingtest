t = int(input())
list1 = [input().split() for _ in range(t)]
for case in list1:
    for letter in case[1]:
        print(letter * int(case[0]), end = '')
    print()
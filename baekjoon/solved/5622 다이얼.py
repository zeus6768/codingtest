word = input()

def dial(l):
    if 'A' <= l <= 'C':
        return 3
    elif 'D' <= l <= 'F':
        return 4
    elif 'G' <= l <= 'I':
        return 5
    elif 'J' <= l <= 'L':
        return 6
    elif 'M' <= l <= 'O':
        return 7
    elif 'P' <= l <= 'S':
        return 8
    elif 'T' <= l <= 'V':
        return 9
    elif 'W' <= l <= 'Z':
        return 10

result = 0
for l in word:
    result += dial(l)

print(result)
'''
1은 2초, 2는 3초 ... 9는 10초, 0은 11초


'''
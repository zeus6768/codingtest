n = int(input())

def hansu(str_num):
    count = 0
    for i in range(1, str_num + 1):
        i = str(i)
        if len(i) < 3:
            count += 1
        else:
            if int(i[0]) - int(i[1]) == int(i[1]) - int(i[2]):
                count += 1
    return count

print(hansu(n))
    
'''입력
1) 110
>>> 99
2) 1
>>> 1
3) 210
>>> 105
4) 1000
>>> 144
'''
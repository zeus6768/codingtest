a, b, arr = 0, 0, []
while True:
    try : 
        a, b = map(int, input().split())
        arr.append(a + b)
    except :
        [print(num) for num in arr]
        break
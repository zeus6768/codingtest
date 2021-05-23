s = input()
alphabet = [chr(i) for i in range(97, 123)]

for char in alphabet:
    try:
        print(s.index(char), end = ' ')
    except:
        print("-1", end = ' ')
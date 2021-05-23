word = input().upper()
list1 = [0] * 26
for letter in word:
    list1[ord(letter) - 65] += 1
if list1.count(max(list1)) > 1:
    print("?")
else:
    print(chr(list1.index(max(list1)) + 65))

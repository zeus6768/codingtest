n = int(input())
words = [input() for i in range(n)]
def is_group(word):
    for letter in word:
        n = word.count(letter)
        if word.find(letter * n) == -1:
            return 0
    return 1
count = 0
for word in words:
    count += is_group(word)
print(count)

'''입력
1)
3
happy
new
year
>>> 3
2)
4
aba
abab
abcabc
a
>>> 1
'''
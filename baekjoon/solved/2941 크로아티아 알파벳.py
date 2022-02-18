croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
for alphabet in croatian:
    if alphabet in word:
        word = word.replace(alphabet, '1')
print(len(word))

'''입력
1) ljes=njak
>>> 6
2) ddz=z=
>>> 3
3) nljj
>>> 3
4) c=c=
>>> 2
'''
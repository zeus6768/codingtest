from collections import Counter
a = 'ccccabcabbbccccbbbdbdb'
b = {'a': 1, 'b': 2, 'c': 3, 'd': 2}
c = Counter(a).most_common()
print(sorted(c, key=lambda x: (-x[1], x[0])))

print(sorted(b, key=lambda x: (-b[x], x)))
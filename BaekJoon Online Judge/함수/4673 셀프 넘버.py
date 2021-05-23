list1 = [i for i in range(1, 10001)]
list2 = []

def self_number(n):
    n = str(n)
    result = int(n)
    for j in range(len(n)):
        result += int(n[j])
    return result

k = 1
while k <= 10000:
    list2.append(self_number(k))
    k += 1

list3 = sorted(list(set(list1) - set(list2)))
[print(l) for l in list3]
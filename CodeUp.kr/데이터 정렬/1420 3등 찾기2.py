import operator

friends_dic = {}
friends_list = []

n = int(input())
for i in range(n):
    name, score = input().split()
    friends_dic[name] = int(score)

friends_list = sorted(friends_dic.items(), key = operator.itemgetter(1))
print(friends_list[-3][0])
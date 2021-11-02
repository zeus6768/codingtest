import sys
read = sys.stdin.readline
n = int(read())
seq = list(map(int, read().split()))
sub_length = [0] * n
for i in range(n):
	for j in range(i):
		pass



# 10 30 20 25 27 50
#  1  2  2 2+1












#지수 코드
# import sys
# input = sys.stdin.readline
# n = int(input())
# l = list(map(int, input().split()))
# l2 = [0] * n
# # def find(num) :
# #     l2[num] = max([l2[i] + 1 for i in range(num) if l[i] < l[num]] + [1])
# # [find(i) for i in range(n)]
# # print(max(l2))


# for i in range(n):
# 	temp = [1]
# 	for j in range(i):
# 		if l[j] < l[i]:
# 			temp.append(l2[j] + 1)
# 	l2[i] = max(temp)
# print(max(l2))

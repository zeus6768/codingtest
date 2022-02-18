import sys
input = sys.stdin.readline

n, m = map(int, input().split())
work_list = [list(map(int, input().split())) for _ in range(n)]
cost = 0

info1 = {}
for work in work_list: 
	info1[work[0]] = info1[work[0]] + 1 if work[0] in info1 else 1

pile = []
while work_list:
	off = False
	work = work_list.pop(0)
	for info in info1:
		if info1[info] and info > work[0]:
			off = True
			cost += work[1]
			work_list.append(work)
			break
	if not off:
		cost += work[1]
		info1[work[0]] -= 1
		pile.append(work)


for i in range(len(pile)-1):
	for j in range(len(pile)-1-i):
		if (pile[j][0] == pile[j+1][0]) and (pile[j][1] < pile[j+1][1]):
			cost += pile[j][1] * 2
			pile[j], pile[j+1] = pile[j+1], pile[j]

print(cost)
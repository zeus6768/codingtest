import sys

def input():
	return sys.stdin.readline().strip()

K, L = map(int, input().split())
wait_list = dict()
order = 0
for _ in range(L):
	order += 1
	student_number = input()
	wait_list[student_number] = order

wait_list = sorted(wait_list, key=lambda x: wait_list[x])
[print(wait_list[i]) for i in range(min(K, len(wait_list)))]
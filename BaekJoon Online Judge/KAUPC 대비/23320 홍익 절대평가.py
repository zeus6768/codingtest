import sys
input = sys.stdin.readline

n = int(input())
scores = sorted(list(map(int, input().split())))
rel_a_rate, abs_min_score = map(int, input().split())

# 상대평가 시 A학점을 받는 학생의 수
int(n * rel_a_rate / 100)

# 절대평가 시 A학점을 받는 학생의 수 
count = 0
for num in scores:
	if abs_min_score <= num:
		count += 1

print(n*rel_a_rate//100, count)

# 지수 코드
# import sys
# input = sys.stdin.readline
# n = int(input())
# s = list(map(int, input().split()))
# r, ms = map(int, input().split())
# print(n*r//100, len([True for i in s if i >= ms]))
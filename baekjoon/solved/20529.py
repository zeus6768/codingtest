from itertools import combinations as cb
import sys

def input():
	return sys.stdin.readline()

def solve():

	for _ in range(T):
		N = int(input())
		MBTIs = input().split()

		pigeon = (N-1)/16
		if pigeon >= 2:
			print(0)
			continue
		
		min_distance = 12
		for a, b, c, in cb(MBTIs, 3):
			distance = 0
			distance += get_distance(a, b)
			distance += get_distance(b, c)
			distance += get_distance(c, a)
			min_distance = min(min_distance, distance)

		print(min_distance)

def get_distance(mbti_1, mbti_2):
	mbti_1 = MBTI_VALUES.get(mbti_1)
	mbti_2 = MBTI_VALUES.get(mbti_2)
	return MBTI_DIFFS[mbti_1][mbti_2]

def get_diff(mbti_1, mbti_2):
	return sum(m1!=m2 for m1, m2 in zip(mbti_1, mbti_2))

T = int(input())

MBTI_NAMES = (
	"ESTJ", "ESTP", 
	"ESFJ", "ESFP",
	"ENTJ", "ENTP",
	"ENFJ", "ENFP",
	"ISTJ", "ISTP",
	"ISFJ", "ISFP",
	"INTJ", "INTP",
	"INFJ", "INFP"
)

MBTI_VALUES = {MBTI_NAMES[i]: i for i in range(16)}
MBTI_DIFFS = tuple(tuple(get_diff(MBTI_NAMES[i],MBTI_NAMES[j]) for j in range(16)) for i in range(16))

solve()

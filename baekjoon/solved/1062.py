from itertools import combinations as cb
import sys

def input():
	return sys.stdin.readline().strip()

def is_countable(part):
	for p in part:
		if not checked[ord[p]]:
			return 0
	return 1

def check(word):
	for w in word:
		checked[ord(w)] = True

def uncheck(word):
	for w in word:
		checked[ord(w)] = False

def is_countable(word):
	for w in word:
		if not checked[ord(w)]:
			return False
	return True

def count():
	global answer
	total = sum(is_countable(word) for word in words)
	answer = max(answer, total)

def find():
	for letters in cbs:
		check(letters)
		count()
		uncheck(letters)
	

if __name__ == "__main__":
	
	base = {'a', 'c', 'i', 'n', 't'}
	alphabets = set(chr(i) for i in range(97, 123)) - base
	checked = [False]*123
	
	N, K = map(int, input().split())
	if K < 5:
		print(0)
		exit(0)
	K -= 5

	words = tuple(set(input()[4:-4])-base for _ in range(N))
	cbs = tuple(cb(alphabets, K))

	answer = 0

	find()

	print(answer)
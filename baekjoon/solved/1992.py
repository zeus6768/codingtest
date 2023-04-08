import sys

def input():
	return sys.stdin.readline().strip()

def solve():
	compress(N, image)
	print(answer)

def compress(size, image):

	global answer

	if whole(image):
		answer += image[0][0]
		return
	
	answer += '('
	ns = size//2
	for i in range(4):
		if i == 0:
			img = [image[j][:ns] for j in range(ns)]
		if i == 1:
			img = [image[j][ns:] for j in range(ns)]
		if i == 2:
			img = [image[ns+j][:ns] for j in range(ns)]
		if i == 3:
			img = [image[ns+j][ns:] for j in range(ns)]
		compress(ns, img)
	answer += ')'

def whole(image):
	prev = image[0][0]
	for i in range(len(image)):
		for j in range(len(image)):
			if prev != image[i][j]:
				return False
			prev = image[i][j]
	return True

if __name__ == "__main__":
	N = int(input())
	image = [input() for _ in range(N)]
	answer = str()
	solve()
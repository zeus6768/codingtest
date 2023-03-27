def input():
	return __import__('sys').stdin.readline()

def main():
	global white, blue
	cut_paper(N, papers)
	print(f"{white}\n{blue}")
	return

def cut_paper(size, paper):
	global white, blue
	if whole(paper):
		if paper[0][0]:
			blue += 1
		else:
			white += 1
		return
	for i in range(4):
		if i == 0:
			p = [paper[j][:size//2] for j in range(size//2)]
		elif i == 1:
			p = [paper[i][size//2:] for i in range(size//2)]
		elif i == 2:
			p = [paper[size//2+i][:size//2] for i in range(size//2)]
		else:
			p = [paper[size//2+i][size//2:] for i in range(size//2)]
		cut_paper(size//2, p)

def whole(paper:list) -> bool:
	prev = paper[0][0]
	for i in range(len(paper)):
		for j in range(len(paper)):
			if prev != paper[i][j]:
				return False
			prev = paper[i][j]
	return True

if __name__ == "__main__":
	N = int(input())
	papers = [list(map(int, input().split())) for _ in range(N)]
	white, blue = 0, 0
	main()
import sys

def input():
	return sys.stdin.readline()

def solve():
	get_num_of_papers(papers)
	answer[0], answer[1], answer[2] = answer[2], answer[0], answer[1]
	[print(a) for a in answer]

def same_number(p:list):
	prev = p[0][0]
	for i in range(len(p)):
		for j in range(len(p)):
			if prev != p[i][j]:
				return False
			prev = p[i][j]
	return True

def get_num_of_papers(paper):
	if same_number(paper):
		p = paper[0][0]
		answer[p] += 1
		return
	
	for i in range(3):
		for j in range(3):
			np = get_paper(i, j, paper)
			get_num_of_papers(np)

def get_paper(x, y, paper):
	size = len(paper)//3
	return [paper[x*size+i][y*size:y*size+size] for i in range(size)]

if __name__ == "__main__":
	N = int(input())
	papers = [tuple(map(int, input().split())) for _ in range(N)]
	answer = [0, 0, 0]
	solve()
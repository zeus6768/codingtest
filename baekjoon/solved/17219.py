import sys

def input():
	return sys.stdin.readline()

if __name__ == "__main__":
	N, M = map(int, input().split())
	url_pw = dict()
	for _ in range(N):
		url, pw = input().split()
		url_pw[url] = pw
	for _ in range(M):
		url = input().strip()
		print(url_pw[url])
from sys import stdin
input = stdin.readline

def main():
	for _ in range(int(input())):
		n, m = map(int, input().split())
		docs = [*map(int, input().split())]
		seq = [*range(n)]
		count = 0
		while docs:
			if (len(docs) > 1) and (docs[0] < max(docs[1:])):
				docs.append(docs.pop(0))
				seq.append(seq.pop(0))
			else:
				count += 1
				docs.pop(0)
				if seq.pop(0) == m:
					break
		print(count)
		
main()
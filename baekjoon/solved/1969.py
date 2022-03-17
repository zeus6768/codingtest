from sys import stdin
input = stdin.readline

def main():
	n, m = map(int, input().split())
	dna = [input() for _ in range(n)]
	result = ""
	for i in range(m):
		count = {}
		for d in dna:
			if d[i] in count:
				count[d[i]] += 1
			else:
				count[d[i]] = 1
		result += sorted(count, key=lambda x: (-count[x], x))[0]

	total = 0
	for j in range(n):
		for k in range(m):
			if result[k] != dna[j][k]:
				total += 1

	print(f"{result}\n{total}")

main()
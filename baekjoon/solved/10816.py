def main():
	input()
	cards = input().split()
	input()
	M = input().split()
	count = {i:0 for i in M}
	for num in cards:
		if num in count:
			count[num] += 1
	result = [str(count[m]) for m in M]
	print(" ".join(result))
main()
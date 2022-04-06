input = __import__('sys').stdin.readline

def vps(string):
	string = list(string)
	cnt = 0
	while string:
		if string.pop() == ')':
			cnt += 1
		else:
			if cnt:
				cnt -= 1
			else:
				return "NO"
	return "NO" if cnt else "YES"

def main():
	[print(vps(input().strip())) for _ in range(int(input()))]
	return

main()
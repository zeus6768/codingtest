input = __import__('sys').stdin.readline

def main():
	n = int(input())
	user = [input().split() + [i] for i in range(n)]
	user = sorted(user, key=lambda x: (int(x[0]), x[2]))
	[print(age, name) for age, name, _ in user]

main()
input = lambda: __import__('sys').stdin.readline().strip()
def main():
	while True:
		num = input()
		if num == '0': break
		print('yes') if num == num[::-1] else print('no')
main()
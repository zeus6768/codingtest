# 문자열 사용 방법
def decom(n: int):
	return n + sum(map(int, list(str(n))))

def main():
	n = int(input())
	for i in range(n):
		if decom(i) == n:
			return i
	return 0

print(main())
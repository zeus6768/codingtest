n = int(input())
num = 665
while n:
	num += 1
	n -= 1 if '666' in str(num) else 0
print(num)
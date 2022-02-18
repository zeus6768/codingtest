import sys

c = int(sys.stdin.readline().rstrip())

def seven_to_three(num):
	reverse = ''
	while num > 0:
		mod = num % 7
		num = num // 7
		reverse += str(mod)
	return reverse[::-1]

def chili_level(n):
	result = seven_to_three(n)
	return int(result, 3)

answer = chili_level(c)
print(answer)



# 함유량 7은 3진법으로 10(3) = 3 단계
# 왜냐, (7**0*0 + 7**1*1) 이기 때문.
# 함유량 14는 (7**0*0 + 7**1*2) 이므로 3진법으로 20(3) = 6 단계
# 254 = 10**0*4 + 10**1*5 + 10**2*2

# 지수
n = int(input())
i, s = 13, ""
while i >= 0:
    t, n = divmod(n, 7 ** i)
    s += str(t)
    i -= 1
print(int(s,3))

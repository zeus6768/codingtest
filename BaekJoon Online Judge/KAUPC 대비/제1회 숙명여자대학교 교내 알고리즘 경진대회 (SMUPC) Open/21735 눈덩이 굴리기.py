n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
len_list = [0] * (2**m)
# 0) 인덱스 + 1 ; 눈크기 + 앞마당[인덱스]
# 1) 인덱스 + 2 ; 눈크기 // 2 + 앞마당[인덱스]
# if m = 1:
# '0' => '1'
def 눈덩이굴리기(n:int, m:int, a:list, len_list:list):
	for i in range(2**m): # i == 0
		method = f"%0{m}d" % int(bin(i)[2:]) # method == "0"
		size = 1
		index = 0
		for bi in method: # bi == "0"
			if bi == '0':
				index += 1
				if index > n:
					break
				size += a[index]
			else:
				index += 2
				if index > n:
					break
				size = (size // 2) + a[index]
		len_list[i] = size
	return max(len_list)

정답 = 눈덩이굴리기(n, m, a, len_list)
print(정답)

# print(method, b, index, a[index], size)

# 지수 코드
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))

def dfs(s, current, time) :
    if s > 0 : current += a[s-1]
    if time == m or s >= n: return current
    s1 = dfs(s+1, current, time+1) if s+1 <= n else 0
    s2 = dfs(s+2, current//2, time+1) if s+2 <= n else 0
    return max(s1, s2)

print(dfs(0, 1, 0))
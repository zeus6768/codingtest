from collections import Counter
input = __import__('sys').stdin.readline
n = int(input())
nums = [int(input()) for _ in range(n)]
counter = Counter(nums)
mc = sorted(counter.most_common(), key=lambda x: (-x[1], x[0]))
print(round(sum(nums)/n))
print(sorted(nums)[n//2])
print(mc[1][0]) if (len(mc)>1 and mc[0][1]==mc[1][1]) else print(mc[0][0])
print(max(nums)-min(nums))

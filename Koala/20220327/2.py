n, s = map(int, input().split())
cows = sorted([int(input()) for _ in range(n)])
left, right, count = 0, 1, 0

while left < n-1:
    total = cows[left] + cows[right]
    if total <= s:  
        count += 1
        right += 1
        if right >= n : 
            left += 1
            right = left+1
    else:
        left += 1
        right = left+1
    
print(count)
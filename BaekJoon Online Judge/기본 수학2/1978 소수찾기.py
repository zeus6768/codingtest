n = int(input())
nums = list(map(int, input().split()))

def isPrime(num):
    if num == 1:
        return 0
    elif num % 2 == 0 and num != 2:
        return 0
    else:
        for i in range(2, int(num / 2)):
            if num % i == 0:
                return 0
        return 1

result = 0
for num in nums:
    result += isPrime(num)

print(result)
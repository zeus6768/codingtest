def binary(num):
    if num <= 1:
        return str(num)
    else:
        return binary(num // 2) + str(num % 2)
    
number = int(input())

result = binary(number)
print(result)
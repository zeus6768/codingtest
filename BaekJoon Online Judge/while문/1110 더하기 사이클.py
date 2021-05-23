number = int(input())
origin_number, new_number, cycle = number, 100, 0
while origin_number != new_number:
    n_10, n_01 = number // 10, number % 10
    new_number = int(str(n_01) + str((n_10 + n_01) % 10))
    number = new_number
    cycle += 1
print(cycle)
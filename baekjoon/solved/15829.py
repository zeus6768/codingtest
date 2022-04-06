input()
s = input()
sum_ = sum([(ord(s[i])-96)*31**i for i in range(len(s))])
print(sum_ % 1234567891)
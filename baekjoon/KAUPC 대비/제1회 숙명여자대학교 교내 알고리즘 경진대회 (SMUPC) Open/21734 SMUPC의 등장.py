s = input()
ascii = [] # [7, 10, 9...]
for k in s: # k = "s" 시작
	ascii_value = ord(k)
	ascii_value = str(ascii_value)
	count = 0
	for m in ascii_value:
		count += int(m)
	ascii.append(count)

[print(s[n]*ascii[n]) for n in range(len(s))]

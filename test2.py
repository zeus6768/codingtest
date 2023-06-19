def get_bitmap(num: str) -> tuple:
	if num == ' ':
		return blank
	return numbers[int(num)]

def solution(word):
	answer = [0] * 32 * ((len(word)-1)//4 + 1)
	for i, w in enumerate(word):
		k = i // 4
		bitmap_number = get_bitmap(w)
		for j in range(8):
			answer[4*j+k] |= bitmap_number[j] << 24 - (8*i)
	answer = list(map(lambda x: "0x" + format(x, '08X'), answer))
	return answer

blank = (0,) * 8

one = (
	0b00001000,
	0b00011000,
	0b00001000,
	0b00001000,
	0b00001000,
	0b00001000,
	0b00001000,
	0b00011100
)

two = (
	0b00111100,
	0b01000010,
	0b10000001,
	0b00000010,
	0b00011100,
	0b00100000,
	0b01000000,
	0b11111111
)

three = (
	0b01111110,
	0b10000001,
	0b00000010,
	0b00011100,
	0b00000010,
	0b00000001,
	0b10000001,
	0b01111110
)

four = (
	0b00000100,
	0b00001100,
	0b00010100,
	0b00100100,
	0b01000100,
	0b10000100,
	0b11111111,
	0b00000100
)

five = (
	0b11111111,
	0b10000000,
	0b10000000,
	0b11111100,
	0b00000010,
	0b00000001,
	0b10000001,
	0b01111110
)

six = (
	0b01111110,
	0b10000000,
	0b10000000,
	0b10000000,
	0b11111110,
	0b10000001,
	0b10000001,
	0b01111110
)

seven = (
	0b01111111,
	0b00000010,
	0b00000100,
	0b00001000,
	0b00010000,
	0b00100000,
	0b01000000,
	0b00000000
)

eight = (
	0b01111110,
	0b10000001,
	0b10000001,
	0b01111110,
	0b10000001,
	0b10000001,
	0b10000001,
	0b01111110,
)

nine = (
	0b01111110,
	0b10000001,
	0b10000001,
	0b10000001,
	0b11111111,
	0b00000001,
	0b00000001,
	0b01111110
)

zero = (
	0b00111100,
	0b01000010,
	0b10000001,
	0b10000001,
	0b10000001,
	0b10000001,
	0b01000010,
	0b00111100
)

numbers = (zero, one, two, three, four, five, six, seven, eight, nine)

r = solution("45678")
for i in range(32):
	if (i+1)%4 == 0:
		print(r[i])
	else:
		print(r[i], end=', ')

# 입력 "12   34"
# answer[0] = one[0] << 24
# answer[4] = one[1] << 24
# ...
# answer[28] = one[7] << 24
#
# answer[0] = two[0] << 16
# ...
# answer[28] = two[7] << 16
# 
# blank()
# blank()
#
# answer[1] = three[0] << 24
# ...
# answer[29] = three[7] << 24
# 
# ...
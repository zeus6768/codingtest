def solve():
	n = int(input())
	bin(0b1000001^0b1111111111111111111111111111111+0b01)

n = int(input())
n = bin(n)[2:]
org = [0] * 32
lenN = len(n)
org[32 - lenN : ] = map(int, n)
bit = [1] * 32
for i in range(1, len(n) + 1):
    bit[-i] = 0 if int(n[-i]) else 1
for i in range(1, 33):
    if not bit[-i]:
        bit[-i] = 1
        break
    bit[-i] = 0
cnt = 0
for i in range(32):
    if org[i] != bit[i]:
        cnt += 1
print(cnt)
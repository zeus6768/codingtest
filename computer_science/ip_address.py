# ip주소와 비트마스크 개수가 주어진다.
# 게이트웨이와 호스트 주소 범위의 최솟값과 최댓값을 리턴하는 함수를 구현하라. 
# 진수 변환을 직접 구현하라. 

def check_format(address: str, bitmask: int) -> bool:
	ip_address = address.split('.')
	if len(ip_address) != 4:
		return False
	for value in ip_address:
		if not (0 <= int(value) < 256):
			return False
	if bitmask < 8:
		return False
	return True

def get_ip(address: str) -> int:
	address = list(map(int, address.split('.')))
	return sum(address[i] << 24-(i*8) for i in range(4))

def get_subnet_mask(bitmask: int) -> int:
	return (2**bitmask-1) << (32-bitmask)

def to_base10(ip: int) -> str:
	return '.'.join(str(ip >> 24-(i*8) & 255) for i in range(4))

def solve(ip_address: str, bitmask: int) -> list:
	if not check_format(ip_address, bitmask):
		return ["ERROR"]
	ip = get_ip(ip_address)
	subnet_mask = get_subnet_mask(bitmask)
	network_address = ip & subnet_mask
	gateway = network_address + 1
	min_host_ip = gateway + 1
	max_host_ip = network_address | 2**(32-bitmask)-1
	return [to_base10(gateway), to_base10(min_host_ip), to_base10(max_host_ip)]

case_1 = ("125.100.1.10", 8)
case_2 = ("192.168.1.129", 25)

print(solve(case_1[0], case_1[1]))
print(solve(case_2[0], case_2[1]))
def solve() -> None:
	closest, diff = get_closest()
	answer = min(abs(N-100), log_10(closest)+diff)
	print(answer)

def get_closest() -> tuple[int]:
	closest, diff = float('inf'), float('inf')
	for channel in CHANNELS:
		d = abs(N - channel)
		if d < diff:
			closest = channel
			diff = d
	return closest, diff

def gen_channels() -> list[int]:

	def _gen_channels(now, depth) -> None:
		result.append(now)
		if depth == DIGITS+1:
			return
		[_gen_channels(now*10+B, depth+1) for B in BUTTONS]

	result = list()
	[_gen_channels(b, 1) for b in BUTTONS]
	result.sort()
	return result

def log_10(n) -> int:
	result = 1
	while n>=10:
		n //= 10
		result += 1
	return result
	
if __name__ == "__main__":
	N = int(input())
	M = int(input())
	BROKEN = list(map(int, input().split())) if M else list()

	BUTTONS = set(range(0, 10)) - set(BROKEN)

	DIGITS = log_10(N)
	CHANNELS = gen_channels()
	
	solve()


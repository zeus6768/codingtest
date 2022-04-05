from collections import deque

def main():
	n = int(input())
	cards = deque(range(n))
	switch, result = False, 0
	while cards:
		if switch:
			cards.append(cards.popleft())
			switch = False
		else:
			result = cards.popleft()
			switch = True
	print(result+1)
	
main()
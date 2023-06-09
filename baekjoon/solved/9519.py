from collections import deque

def mix(indices) -> list:
	new_indices = list()
	if size % 2:
		first_half, second_half = deque(indices[:size//2+1]), indices[size//2+1:]
	else:
		first_half, second_half = deque(indices[:size//2]), indices[size//2:]
	while first_half or second_half:
		if first_half:
			new_indices.append(first_half.popleft())
		if second_half:
			new_indices.append(second_half.pop())
	return new_indices

def get_reps():
	reps = 1
	new_indices = mix(indices)
	while indices != new_indices:
		new_indices = mix(new_indices)
		reps += 1
	return reps

X = int(input())
word = input()

answer = str()

size = len(word)
indices = list(range(size))

reps = get_reps()

for i in range(reps-X%reps):
	indices = mix(indices)

for idx in indices:
	answer += word[idx]

print(answer)

"""
0 1 2
>>> 0 2 1
>>> 0 1 2

0 1 2 3
>>> 0 3 1 2
>>> 0 2 3 1
>>> 0 1 2 3

0 1 2 3 4
>>> 0 4 1 3 2
>>> 0 2 4 3 1
>>> 0 1 2 3 4

0 1 2 3 4 5
>>> 0 5 1 4 2 3
>>> 0 3 5 2 1 4
>>> 0 4 3 1 5 2
>>> 0 2 4 5 3 1
>>> 0 1 2 3 4 5

0 1 2 3 4 5 6
>>> 0 6 1 5 2 4 3
>>> 0 3 6 4 1 2 5
>>> 0 5 3 2 6 1 4
>>> 0 4 5 1 3 6 2
>>> 0 2 4 6 5 3 1
>>> 0 1 2 3 4 5 6

0 1 2 3 4 5 6 7
>>> 0 7 1 6 2 5 3 4
>>> 0 4 7 3 1 5 6 2
>>> 0 2 4 6 7 5 3 1
>>> 0 1 2 3 4 5 6 7
"""
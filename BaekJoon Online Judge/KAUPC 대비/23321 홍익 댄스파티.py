import sys
input = sys.stdin.readline

table = ['.o', 'ow', 'ml', 'ln', 'n.']

pics = [input().rstrip() for _ in range(5)]

착석열 = [i for i, p in enumerate(pics[2]) if p == "o"]


for i, pic in enumerate(pics):
	new_pic = ""
	for j, p in enumerate(pic):
		if j in 착석열:
			new_pic += p
		else:
			if p == table[i][0]:
				new_pic += table[i][1]
			else:
				new_pic += table[i][0]
	print(new_pic)
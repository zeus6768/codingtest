def act(action):
	if action in ('R', 'L'):
		rotate(action)
	if action == 'F':
		forward()

def rotate(action):
	global d
	if action == 'R':
		d += 1
	else:
		d -= 1
	d %= 4
	
def forward():
	global d, now, min_x, min_y
	now[0], now[1] = now[0]+SWNE[d][0], now[1]+SWNE[d][1]
	min_x, min_y = min(min_x, now[0]), min(min_y, now[1])
	visited.append([now[0], now[1]])

def proceed():
	global max_x, max_y
	if min_x < 0 and min_y < 0:
		for xy in visited:
			xy[0] -= min_x
			xy[1] -= min_y
	elif min_x < 0:
		for xy in visited:
			xy[0] -= min_x
	elif min_y < 0:
		for xy in visited:
			xy[1] -= min_y
	for xy in visited:
		max_x = max(max_x, xy[0])
		max_y = max(max_y, xy[1])

input()
actions = input()

SWNE = ((1, 0), (0, -1), (-1, 0), (0, 1))
d = 0
now = [0, 0]
visited = [[0, 0]]

min_x, min_y, max_x, max_y = 50, 50, 0, 0

[act(action) for action in actions]
proceed()

maze = [['#'] * (max_y+1) for _ in range(max_x+1)]

for v in visited:
	x, y = v
	maze[x][y] = '.'

[print(''.join(m)) for m in maze]
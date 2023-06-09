import sys

def input():
	return sys.stdin.readline()

def get_color_diff(color_1, color_2):
	return sum(abs(color_1[i]-color_2[i]) for i in range(3))

def add_color(color_1, color_2):
	return tuple(color_1[i]+color_2[i] for i in range(3))

def mix(idx, count, color):

	global answer

	if count > 1:
		mixed_color = tuple(map(lambda x: x//count, color))
		answer = min(answer, get_color_diff(target, mixed_color)) 
	
	if count == 7:
		return
	
	[mix(i+1, count+1, add_color(color, colors[i])) for i in range(idx, N)]

N = int(input())
colors = [tuple(map(int, input().split())) for _ in range(N)]
target = tuple(map(int, input().split()))

answer = float("INF")

mix(0, 0, (0, 0, 0))

print(answer)
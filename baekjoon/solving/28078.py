import sys
from collections import deque

class Queue():

	ANGLE_0 = 0
	ANGLE_90 = 90
	ANGLE_180 = 180
	ANGLE_270 = 270

	def __init__(self) -> None:
		self.queue = deque()
		self.angle = Queue.ANGLE_0

	def push(self, query):
		if query == 'b':
			...
		elif query == 'w':
			queue.appendleft(WALL)

def input():
	return sys.stdin.readline()

queue = deque()
BALL, WALL = "BALL", "WALL"

Q = int(input())

for _ in range(Q):

	query = input().split()


	
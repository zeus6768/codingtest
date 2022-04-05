import sys
input = sys.stdin.readline

def main():
	r, c = map(int, input().split())
	map_ = [input().split() for _ in range(r)]

	print(map_)
	
main()

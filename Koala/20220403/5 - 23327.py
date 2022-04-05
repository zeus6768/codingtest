input = __import__("sys").stdin.readline

def main():
	_, q = map(int, input().split())
	psum1, psum2 = [0], [0]
	for t in [*map(int, input().split())]:
		psum1.append(psum1[-1]+t)
		psum2.append(psum2[-1]+t**2)
	for _ in range(q):
		l, r = map(int, input().split())
		result = ((psum1[r]-psum1[l-1])**2 - (psum2[r]-psum2[l-1]))//2
		print(result)

main()

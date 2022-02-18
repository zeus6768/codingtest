arr = list(map(int, input().split()))
sarr = set(arr)

if len(sarr) == 1:
	print(10000 + 1000*arr[0])
elif len(sarr) == 2:
	for i in sarr: arr.remove(i)
	print(1000+ arr[0]*100)
else:
	print(100 * max(arr))
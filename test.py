import time
a = list(range(100000))

start = time.time()
a.reverse()
#a[::-1]
end = time.time()
print(end - start)
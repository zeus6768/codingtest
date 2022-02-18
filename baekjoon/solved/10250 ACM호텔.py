t = int(input())
h_w_n = [tuple(map(int, input().split())) for i in range(t)]
for test in h_w_n:
    h, w, n = test[0], test[1], test[2]
    a, b = n // h, n % h
    if a * h < n <= (a + 1) * h:
        room_number = a + 1
        room_floor = b
    else:
        room_number = a
        room_floor = h
    print(f"{room_floor}{room_number:02}")


# 1 걷는 거리가 짧을수록 선호
# 2 층이 낮을수록 선호
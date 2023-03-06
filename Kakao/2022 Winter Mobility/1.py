def solution(infos, m):

	car_time, bike_time, public_time, walk_time = [0] * 4
	bike_walk, public_walk = 0, 0

	for info in infos:
		
		# 자동차만
		car_time += info[0]

		# 자전거 + 도보
		bike = info[1]
		walk = float("inf") if m < bike_walk+info[3] else info[3]
		if bike <= walk:
			bike_time += bike
			bike_walk = 0
		else:
			bike_time = walk
			bike_walk += walk

		# 대중교통 + 도보
		public = info[2] if info[2] != -1 else float("inf")
		walk = float("inf") if m < public_walk+info[3] else info[3]
		if public <= walk:
			public_time += public
			public_walk = 0
		else:
			public_time = walk
			public_walk += walk

		# 도보
		if walk_time + info[3] < m:
			walk_time += info[3]
		else:
			walk_time = float("inf")
	
	return min(car_time, bike_time, public_time, walk_time)


infos = [[100, 80, 10, 20], [120, 60, -1, 40]]

m = 30

result = solution(infos, m)
print(result)
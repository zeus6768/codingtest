def to_day(ymd: str):
	y, m, d = map(int, ymd.split())
	return y*360 + m*30 + d

def get_month_off(work_day):
	return min(36, work_day // 30)

def get_year_off(work_year):
	result = 0
	for i in range(work_year):
		A = i // 2
		result += A + 15
	return result

def solve():
	S = to_day(input())
	E = to_day(input())

	work_day = E - S
	work_year = work_day//360

	print(get_year_off(work_year), get_month_off(work_day))
	print(f"{work_day}days")

solve()
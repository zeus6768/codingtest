birth = input()
n = int(input())
code_days = [input() for _ in range(n)]
code_days.sort()

def biorythm(birthday, day):
	bio_year = 0
	bio_mon = 0
	bio_day = 0
	for i in range(8):
		if i < 4:
			bio_year += (int(birthday[i])-int(day[i]))**2
		elif i < 6:
			bio_mon += (int(birthday[i])-int(day[i]))**2
		else:
			bio_day += (int(birthday[i])-int(day[i]))**2
	return bio_year * bio_mon * bio_day

bio_date = []
[bio_date.append(biorythm(birth, code_days[i])) for i in range(n)]
max_bio = max(bio_date)
index = bio_date.index(max_bio)
print(code_days[index])

#[이지수] [오전 10:41] 
import sys
input = sys.stdin.readline
b = input()
maxV = 0; day = ""
for _ in range(int(input())) :
    d = input()
    m = [(int(b[i])-int(d[i]))**2 for i in range(8)]
    v = sum(m[0:4])*sum(m[4:6])*sum(m[6:8])
    if maxV < v : (maxV, day) = (v, d)
    elif maxV == v : day = d if d < day else day
print(day)
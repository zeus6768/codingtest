def calc_date(start, time):
    Y, M, D, H, m, S = start
    tD, tH, tm, tS = time

    S += tS
    while S >= 60: 
        m += 1
        S -= 60

    m += tm
    while m >= 60: 
        H += 1
        m -= 60
        
    H += tH
    while H >= 24:
        D += 1
        H -= 24

    D += tD
    while D > 30:
        M += 1
        D -= 30
    
    while M > 12:
        Y += 1
        M -= 12
        
    return Y, M, D, H, m, S


def solution(s, times):
    answer = [1, 0]

    s = [*map(int, s.split(':'))]
    first_date = s[0]*360 + s[1]*30 + s[2]
    last_date = first_date
    print(f"first_date: {first_date}")
    
    for time in times:
        t = [*map(int, time.split(':'))]
        result = calc_date(s, t)
        s = result
        print(s)
        
        new_date = result[0]*360 + result[1]*30 + result[2]

        if new_date - last_date > 1:
            answer[0] = 0

        last_date = new_date
	
    answer[1] = last_date - first_date + 1

    return answer


r1 = solution("2021:04:12:16:08:35", ["01:06:30:00", "01:04:12:00"])
print(r1)
r2 = solution("2021:04:12:16:08:35", ["01:06:30:00", "00:01:12:00"])
print(r2)
r3 = solution("2021:04:12:16:10:42", ["01:06:30:00"])
print(r3)
r4 = solution("2021:04:12:16:08:35", ["01:06:30:00", "01:01:12:00", "00:00:09:25"])
print(r4)
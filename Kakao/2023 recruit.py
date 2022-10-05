# 1번
def solution(today, terms, privacies):
    answer = []
    today = [*map(int, today.split('.'))]

    term = {}
    for t in terms:
        a, b = t.split()
        term[a] = int(b)

    for i, p in enumerate(privacies):
        date, t = p.split()
        date = [*map(int, date.split('.'))]
        y, m, d = date

        if d - 1 == 0:
            m -= 1
            d = 28
        else:
            d = d - 1
        
        nm = m + term[t]
        if nm > 12:
            if nm % 12:
                y += nm // 12
                m = nm % 12
            else:
                y += (nm//12)-1
                m = 12
        else:
            m = nm
            
        if y<today[0] or (y==today[0] and m<today[1]) or (y==today[0] and m==today[1] and d<today[2]):
            answer.append(i+1)

        
    return answer

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

#solution(today, terms, privacies)


# 2번

# 3번
def solution(users, emoticons):

    def get_cases(n, result=[]):
        if len(result)==n:
            emo_cases.append(result[:])
            return
        for i in range(10, 41, 10):
            result.append(i)
            get_cases(n, result)
            result.pop()

    emo_cases = []
    get_cases(len(emoticons))

    results = []
    for case in emo_cases:
        가입자수, 구매비용 = 0, 0
        costs = [0] * len(users)
        for 할인율, 가격 in zip(case, emoticons):
            실가격 = int(가격 * (100-할인율) / 100)
            for i, (기준, 예산) in enumerate(users):
                if 기준 <= 할인율:
                    costs[i] += 실가격

        for i in range(len(users)):
            if users[i][1] <= costs[i]:
                가입자수 +=1
            else:
                구매비용 += costs[i]

        results.append((가입자수, 구매비용))
        
    results.sort(key=lambda x: (-x[0], -x[1]))

    answer = results[0]

    return answer


# 5번
def solution(commands):
    
    answer = []

    addr = [[None]*50 for _ in range(50)]
    vals = [[None]*50 for _ in range(50)]

    for i in range(50):
        for j in range(50):
            addr[i][j] = (i, j)

    for command in commands:

        inst, *args = command.split()

        if inst == "UPDATE":
            if len(args) == 3:
                r, c, value = args
                r, c = int(r)-1, int(c)-1
                x, y = addr[r][c]
                vals[x][y] = value
            else:
                value1, value2 = args
                for i in range(50):
                    for j in range(50):
                        x, y = addr[i][j]
                        if vals[x][y] == value1:
                            vals[x][y] = value2

        elif inst == "MERGE":
            r1, c1, r2, c2 = map(lambda x: int(x)-1, args)
            x1, y1 = addr[r1][c1]
            x2, y2 = addr[r2][c2]
            for i in range(50):
                for j in range(50):
                    if addr[i][j] == (x2, y2):
                        addr[i][j] = (x1, y1)
                        vals[i][j] = None

        elif inst == "UNMERGE":
            r, c = map(lambda x: int(x)-1, args)
            x, y = addr[r][c]
            tmp = vals[x][y]
            for i in range(50):
                for j in range(50):
                    if addr[i][j] == (x, y):
                        addr[i][j] = (i, j)
                        vals[i][j] = None
            vals[r][c] = tmp

        elif inst == "PRINT":
            r, c = map(lambda x: int(x)-1, args)
            x, y = addr[r][c]
            answer.append(vals[x][y]) if vals[x][y] else answer.append("EMPTY")

    return answer
class myClass():

    def __init__(self, k, n):
        self.memo = [[0] * (n + 1) for _ in range(k + 1)]

    def supersum(self, k, n):
        if k == 0:
            return n

        elif self.memo[k][n]:
            return self.memo[k][n]

        result = 0
        for i in range(n):
            result += self.supersum(k - 1, i + 1)

        self.memo[k][n] = result
        
        return result

kn_arr = []
result_arr = []

while True:
    try:
        k, n = map(int, input().split())
        kn_arr.append([k, n])
    except:
        break

for i in range(len(kn_arr)):
    answer = myClass(kn_arr[i][0], kn_arr[i][1])
    result_arr.append(answer.supersum(kn_arr[i][0], kn_arr[i][1]))

for res in result_arr:
    print(res)
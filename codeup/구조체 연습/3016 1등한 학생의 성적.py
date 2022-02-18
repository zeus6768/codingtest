from operator import itemgetter

def rank(name, array, num_of_subject):
    sorted_array = sorted(array, key = itemgetter(num_of_subject), reverse = True)
    for student in sorted_array:
        if name in student:
            for one in sorted_array:
                if student[num_of_subject] == one[num_of_subject]:
                    return sorted_array.index(one) + 1

n = int(input())
arr = [input().split() for i in range(n)]

for student in arr:
  student[1] = int(student[1])
  student[2] = int(student[2])
  student[3] = int(student[3])

# 첫 번째 과목의 1등
first_arr = sorted(arr, key = itemgetter(1), reverse = True)
name = first_arr[0][0]

# 두 번째 과목 기준 내림차순, 순위
second_rank = rank(name, arr, 2)

# 세 번째 과목 기준 내림차순, 순위
third_rank = rank(name, arr, 3)

# 이름, 석차, 석차 출력
print(name, second_rank, third_rank)  # Bae
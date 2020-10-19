progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

import math
def solution(progresses, speeds):
    answer = []

    a = []  # 남은 일 (progresses)
    b = []  # 추가로 필요한 일(days) 수
    for i in range(len(progresses)):
        a.append(100 - progresses[i])
        b.append(math.ceil(a[i] / speeds[i]))

    big = b[0]
    count = 1
    for i in range(1, len(b)):
        if b[i] > big:
            big = b[i]
            answer.append(count)
            count = 1
            if i == len(b) - 1:
                answer.append(count)

        elif b[i] < big:
            count += 1
            if i == len(b) - 1:
                answer.append(count)

        elif b[i] == big:
            count += 1
            if i == len(b) - 1:
                answer.append(count)

    return answer





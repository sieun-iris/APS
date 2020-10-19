def solution(a, b):
    Q = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    A = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    count = 0
    for i in range(len(A)):
        if a == 1 and i == 1:
            return Q[b % 7]
        if i == a:
            break
        else:
            count += A[i]

    answer = Q[((count + b) % 7)]
    return answer
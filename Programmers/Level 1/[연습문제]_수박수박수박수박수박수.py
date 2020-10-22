def solution(n):
    result = [''] * n
    for i in range(0, n):
        if i % 2:
            result[i] = '박'
        else:
            result[i] = '수'
    return ''.join(result)
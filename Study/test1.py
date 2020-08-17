# 리스트 값이 int가 아니면 뺀다. type이 int면 다 더하라

def sum_soldiers(squad_rooms, total):
    count = []
    result = []
    for i in squad_rooms:
        for j in i:
            if j == "-":
                result += [j]
            # else:
            #     result += [j]
    
        a = sum(result)
        # b = len(count)
        # c = a-b

    # if a < total:
    #     return ('문제발생({}명 적음)'.format(b))

    # elif a > total:
    #     return ('문제발생({}명 많음)'.format(b))

    # else:
    #     return '이상없음'

    print(a)

print(sum_soldiers(
    [
        [6, 5, 7, 3, 5, 3, 1, 7, 9],
        [5, '-', 4, 2, 3, 7, 8, 1, 3],
        [3, 9, 1, 5, 3, 9, 4, 2, 6],
        [7, 8, 1, 4, 1, 5, 3, 1, 3],
        [3, 5, 5, 4, '-', 5, 3, 1, 3],
        [5, 5, 4, 2, 3, 7, 8, 1, 3],
        [1, 5, 3, 4, 1, 5, 3, 1, 3],
        [4, 5, 7, 3, '-', 3, 1, 7, 9],
    ],
    288)
)
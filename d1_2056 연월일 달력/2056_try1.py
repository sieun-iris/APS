import sys
# sys.stdin = open('input_data/2056.txt') 경로
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    cal = input()
    year = cal[0:4]
    month = cal[4:6]
    day = cal[6:8]

    if int(month) == 2:
        if int(day) > 28:
            print('#{} -1'.format(t))
        else:
            print('#{} {}/{}/{}'.format(t, year, month, day))

    elif 13 > int(month) > 0 :
        if 32 > int(day) > 0:
            print('#{} {}/{}/{}'.format(t, year, month, day))

    else:
        print('#{} -1'.format(t))





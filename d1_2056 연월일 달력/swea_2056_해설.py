import sys
# sys.stdin = open('input_data/2056.txt') 경로
sys.stdin = open('input.txt', 'r')


def check_month(month):
    # month에는 글자가 담겨있다. month : '02'
    if 0 < int(month) < 13:
        return month
    return ''

def check_day(month, day):
    # day: '28', month: '02'     # key - month : value - day
    day_dict = {    
        '01':31, '02':28,
        '03':31, '04':30,
        '05':31, '06':30,
        '07':31, '08':31,
        '09':30, '10':31,
        '11':30, '12':31,
    }

    if not day_dict.get(month):  # 비어있을 경우, month가 맞을 경우
        return ''

    if 0 < int(day) <= day_dict.get(month):
        return day
    return ''

T = int(input())   # 글자 5가 담겨있는 상황, int로 바꿔야 함

# t = 1, 2, 3, 4, 5
for t in range(1, T+1):
    # 인풋이 한번 더 들어가서 커서가 한 줄씩 내려감
    # 한 줄씩 내려가는게 target에 담긴다
    target = input()

    year, month, day = target[:4], target[4:6], target[6:]
    month = check_month(month)  # month 변수를 생성해서 저장
    day = check_day(month, day)

    if month and day:
        print('#{} {}/{}/{}'.format(t, year, month, day))
    else:
        print('#{} -1'. format(t))

    # result = 0
    # print('#{} {}'.format(t, result))





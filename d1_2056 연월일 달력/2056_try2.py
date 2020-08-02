import sys
# sys.stdin = open('input_data/2056.txt') 경로
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    cal = input()
    year = cal[:4]
    month = cal[4:6]
    day = cal[6:8]

    if month == True:
        if day == True:
            print('#{} {}/{}/{}'.format(t, year, month, day))
    else:
        print('#{} -1'.format(t))


def check_month(month):
    if int(month) == 2:
        if int(day) > 28:
            return False
    elif 13 > int(month) > 0:
        return True

def check_day(day):
    if 32 > int(day) > 0:
        return True
    else:
        return False


    # def check_feb(month, day):
    #     if 13 > int(month) > 0:
    #         if int(month) == 2:
    #             if int(day) > 28:
    #                 return ''
    #         else:
    #             return month
            
    #     elif 32 > int(day) > 0:
    #         return day
    #     else:
    #         return ''
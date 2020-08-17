# 높이 h
# 반복 횟수 r

h = int(input())
r = int(input())

for cnt in range(1, r+1):
    star = ''
    for i in range(1, h+1):
        if i == 1:
            star += '*'
            star += '\n'

        elif h+1 >= i >= 2:
            star += ' ' * (i-1)
            star += '*'
            star += '\n'

    star_2 = ''
    for j in range(h-1, 0, -1):
        if h+1 >= j >= 2:
            star_2 += ' ' * (j-1)
            star_2 += '*'
            star_2 += '\n'

        elif j == 1:
            star_2 += '*'


    print('{}{}'.format(star, star_2))


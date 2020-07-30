# 진행중

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    numbers = list(map(int, input().split())) 

for number in numbers:
    if number == max(numbers):
        if number == min(numbers):
            print('#{} {}'.format(t, '='))

        elif number < max(number):
                print('#{} {}'.format(t, '<'))

        else:
            print('#{} {}'.format(t, '>'))


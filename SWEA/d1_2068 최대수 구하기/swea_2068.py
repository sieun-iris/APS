import sys
sys.stdin = open("input_a.txt", "r")

T = int(input())
for t in range(1, T+1):
    numbers = list(map(int, input().split())) 

    for number in numbers:
        if number == max(numbers):
            print('#{} {}'.format(t, max(numbers)))


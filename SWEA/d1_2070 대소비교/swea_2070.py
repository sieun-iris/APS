import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    a, b = map(int, input().split())
    if a > b:
        print('#{} >'.format(t))
    elif a == b:
        print('#{} ='.format(t))
    else:
        print('#{} <'.format(t))

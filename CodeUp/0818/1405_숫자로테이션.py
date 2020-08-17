import sys
sys.stdin = open('1405_input.txt', 'r')


def rotate(case, i):
    return case[i:] + case[:i]


T = int(input())
case = list(map(int, input().split()))
for i in range(T):
    a = list(map(str, rotate(case, i)))
    print()
    for j in a:
        print(j+' ', end="")

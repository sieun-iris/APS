import sys; sys.stdin = open("2751.txt", "r")

N = int(input())

case = [int(input()) for _ in range(N)]
case.sort()
for i in case:
    print(i)



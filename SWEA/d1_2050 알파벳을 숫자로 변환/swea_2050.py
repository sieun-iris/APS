import sys
sys.stdin = open('input.txt', 'r')

# 방법 1
T = list(input())
for t in range(1, len(T)+1):
    result = t
    print(result, end = ' ')

# 방법 2
T = list(input())
for t in range(len(T)):
    print(ord(T[t])-64, end=' ')

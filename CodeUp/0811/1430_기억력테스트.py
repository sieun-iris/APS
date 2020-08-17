import sys
sys.stdin = open('input_1430.txt', 'r')

a = int(input())
test = list(map(int, input().split()))
b = int(input())
answer = list(map(int, input().split()))


result = ''
for j in answer:
    if j in test:
        result += '1'
    else:
        result += '0'

for k in result:
    print(k, end=' ')


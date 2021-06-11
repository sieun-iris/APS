import sys; sys.stdin = open("14490.txt", "r")

n, m = map(int, input().split(':'))
num = 0
minNum = min(n, m)

for i in range(minNum+1, 1, -1):
    if n % i == 0 and m % i == 0:
        num = i
        break

if num == 0:
    print('{}:{}'.format(n, m))
else:
    print('{}:{}'.format(n//num, m//num))

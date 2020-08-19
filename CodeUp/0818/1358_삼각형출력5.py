# 참고

n = int(input())
for i in range(int(n/2), -1, -1):
    for j in range(0, i):
        print(' ', end='')
    for j in range(0, (n - i * 2)):
        print('*', end='')
    for j in range(0, i):
        print(' ', end='')
    print()
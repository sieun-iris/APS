T = int(input())

for i in range(1, T+1):
    for j in range(0, T):
        print(i*T-j, end=' ')
    print()
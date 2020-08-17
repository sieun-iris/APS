T = int(input())

for i in range(1, T+1):
    for j in range(T):
        print(i+j*T, end=" ")
    print()
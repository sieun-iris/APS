T = int(input())

for i in range(T):
    for j in range(1, T+1):
        print((T*j)-i, end=" ")
    print()
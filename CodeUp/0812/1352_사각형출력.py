T = int(input())

star = []
for t in range(1, T+1):
    star += ['*' * T]
    
for i in star:
    print(i)
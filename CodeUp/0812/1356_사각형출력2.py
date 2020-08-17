T = int(input())

stars = []
for i in range(1, T+1):
    stars += ['*' * T]

result = []
for idx, j in enumerate(stars, 1):
    if idx == 1:
        result += [j]
    elif idx == T:
        result += [j]
    else:
        result += ['*' + ' ' * (T-2) + '*']

for a in result:
    print(a)
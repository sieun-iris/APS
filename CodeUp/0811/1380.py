k = int(input())

result_i = []
result_j = []
for i in range(1, 7):
    for j in range(1, 7):
        if  i + j == k:
            result_i += [i]
            result_j += [j]

for a in result_i:
    for b in result_j:
        if a + b == k:
            print('{} {}'.format(a, b))

# 너무 비효율적으로 짠 것 같다.
# [1, 4, 2, 3, 3, 2, 4, 1] 이후, 이를 두 개씩 문자로 바꾸는 방법을 모르겠다 ㅠ
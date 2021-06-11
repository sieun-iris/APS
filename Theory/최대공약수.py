a = 12
b = 4

num = 0
for i in range(a+1, 1, -1):
    # 큰 수부터 거꾸로 탐색하기 때문에, 먼저 나오는 수가 최대공약수
    # 아래 조건을 성립하는 i가 최대공약수가 됨
    if a % i == 0 and b % i == 0:
        num = i
        break
if num == 0:
    print('{}:{}'.format(a, b))
else:
    print(num)

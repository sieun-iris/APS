import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    numbers = list(map(int, input().split())) 
    # 앞에 작성된 함수를 뒤에 적용하는 것

    for i in range(10):
        sum = sum + numbers[i]

    print("#%d" % (i+1), end=' ')
    print(round(sum/10))
    sum = 0    

    # print(sum(int(result)) / len(result))
    # print('#{} {}'.format(t, result))








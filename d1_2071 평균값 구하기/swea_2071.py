import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    numbers = list(map(int, input().split())) 
    avg_numbers = round(sum(numbers) / len(numbers))
    print('#{} {}'.format(t, avg_numbers))




    # for i in range(10):
    #     sum = sum + numbers[i]
    # print(round(sum/10))
    # sum = 0    

    # print('#{} {}'.format(t, result))








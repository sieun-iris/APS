import sys
sys.stdin = open('1420_input.txt', 'r')

T = int(input())

a = []
score_3 = []

for i in range(1, T+1):
    name, score = list(map(str, input().split()))
    result = {int(score): name}
    a.append(int(score))
    score_3 = sorted(a)
    # print(result)

print(score_3[2])
# print(result)

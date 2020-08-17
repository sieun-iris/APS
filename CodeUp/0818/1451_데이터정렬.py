import sys
sys.stdin = open("1451_input.txt", "r")


def selectionSort(a):
    for i in range(len(a)-1):
        # 5개라면 0, 1, 2, 3까지 4번 도는 것
        # 최소값 찾기
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]  # 맨 앞과 가장 작은 값을 바꿔치기


T = int(input())
test_case = []

for t in range(T):
    number = int(input())
    test_case.append(number)

selectionSort(test_case)
for k in test_case:
    print(k)
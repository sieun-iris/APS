import sys
sys.stdin = open('input.txt', 'r')

a, b = list(map(int, input().split()))
student = list(map(int, input().split()))

def bubbleSort(arr):
    for j in range(0, len(arr) - 1):
        for i in range(j+1, len(arr)):
            if arr[j] > arr[i]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
    return arr
result = bubbleSort(student)

student_1 = ''
for k in result[:b]:
    student_1 += str(k)
    student_1 += ' '

student_2 = ''
for l in result[b:]:
    student_2 += str(l)
    student_2 += ' '

print('{} \n{} '.format(student_1, student_2))





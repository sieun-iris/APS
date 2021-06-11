import sys
sys.stdin = open("input.txt", "r")

student_num = int(input())
student_history = []
student_result = [0] * student_num

for _ in range(student_num):
    student_history.append(list(map(int, input().split())))

for i in range(student_num):
    friend = []
    for j in range(student_num):
        for k in range(student_num):
            if student_history[i][j] == student_history[k][j] and k != i and k not in friend:
                student_result[i] += 1
                friend.append(k)

print(student_result.index(max(student_result))+1)
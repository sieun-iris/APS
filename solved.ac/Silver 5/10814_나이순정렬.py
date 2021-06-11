import sys; sys.stdin = open("10814.txt", "r")

N = int(input())
case = [input() for _ in range(N)]

infos = []
for i in range(N):
    info = [
        int(case[i].split(' ')[0]),  # 나이
        case[i].split(' ')[1],       # 이름
        i+1                          # 순서
    ]
    infos.append(info)

infos.sort(key=lambda x:(x[0], x[2]))
for info in infos:
    print(info[0], info[1])




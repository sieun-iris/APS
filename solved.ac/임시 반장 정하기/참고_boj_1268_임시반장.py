N = int(input())    #학생수N명
data = []           #입력을 2차원 배열로 받으려고 list 하나 만듬
for i in range(N):
    data += [list(map(int, input().split()))]   #입력 받고

captin_list = [0] * N   # 1번학생~N번학생이 만난 학생 수를 captin_list에 넣음
for i in range(N):      # 비교할 학생A  for문돌리고
    count = 0           # 계산 끝나면 count = 0 초기화
    for j in range(N):  # 비교할 학생B for문
        for k in range(5):  #학년 수 5개 for문 돌리고
            if data[i][k] == data[j][k] and i != j: # k학년일때 i학생과 j학생이 같은 반 이면 
                captin_list[i] += 1                     # and i학생과 j학생이 동일인물이 아니면
                break        # i번째 학생의 count 값을 1씩 증가시키고, 한번 만난 학생은 더이상 count할 필요없으므로 break
                            #
print(captin_list.index(max(captin_list))+1)    # 최대값을 가진 인덱스를 구해서 정답출력(index는 0부터이므로 +1)
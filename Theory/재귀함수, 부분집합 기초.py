# 재귀함수
# for i in range(3):
#     print('Hi')

# 재귀 호출로 단순 반복 구현하기
# 재귀 호출이 몇 번 행해졌는지 알 수 있어야 한다.
# 재귀 호출의 종료는 매개변수를 기준으로 판단한다.

# 재귀호출은 내부에 함수 호출을 하는 부분, 함수 호출을 끝내는 부분이 필요하다

# def printHello(i):  # i를 이용해서 종료를 판단
#     if i < 3:   # 기저 사례 (끝내는 부분)
#         print('Hello')
#         printHello(i + 1)
#
# printHello(0)


#####
# 매개변수를 기준으로 종료 판단
# 각 함수마다 자신만의 매개변수를 가져간다

# def printHello(i, n):
#     if i == n:   # 기저 사례 (끝내는 부분)
#         pass
#     else:
#         print(i, 'Hello')  # 함수 호출 이전의 계산작업
#         printHello(i + 1, n)
#         print(i, 'Hello')   # 함수 호출 이후의 작업
#
# printHello(0, 3)

''' 결과
0 Hello
1 Hello
2 Hello
2 Hello
1 Hello
0 Hello
'''


#####
# def printHello(i, n):
#     if i == n:
#         print(arr)
#     else:
#         arr[i] = i
#         printHello(i + 1, n)
#         arr[i] = 0
#
#
# N = 3
# arr = [0] * N
# printHello(0, N)
# print(arr)   # 되돌아오면서 지우는 것  # 출력: [0, 0, 0]
# 출력: [1, 2, 3]



#### 함수 호출 두 번

# cnt = 0   # 전역변수
#
# def printHello(i, n):
#     if i == n:
#         global cnt; cnt += 1
#
#     else:
#         printHello(i + 1, n)
#         printHello(i + 1, n)
#         printHello(i + 1, n)
#
# # printHello(0, 3)    # 함수 호출 세 번, 3을 넘기면 3^3
# N = 3
# printHello(0, N)  # 0, 4 를 하면 16 / 0, 10을 하면 1024
# print(cnt)
# 호출 한 번 하면 1, 두 번 하면 8


#####
# 부분집합
# cnt = 0   # 전역변수
#
# def printHello(i, n):   # 백트레킹을 구현할 때 많이 쓰는 패턴(i와 같이 증가시키는 값이 있음)
#     if i == n:
#         global cnt; cnt += 1
#         print(bits)
#
#     else:
#         bits[i] = 1    # 첫 번째 원소를 포함 / i의 위치에 1을 적는다
#         printHello(i + 1, n)
#
#         bits[i] = 0 # 포함하지 않음
#         printHello(i + 1, n)
#
# bits = [0] * 3
# printHello(0, 3)  # 0, 4 를 하면 16 / 0, 10을 하면 1024
# print(cnt)



####
# 부분집합 for문 표현
bits = [0] * 3
# for i in range(2):
#     bits[0] = i
#     for i in range(2):
#         bits[1] = i
#         for i in range(2):
#             bits[2] = i
#             print(bits)
#
# print('----------')
# def subset(k, n):
#     if k == n:
#         print(bits)
#     else:
#         for i in range(2):
#             bits[0] = i
#             subset(k + 1, n)
#
#         # bits[i] = 0
#         # subset(k + 1, n)
#         # bits[i] = 1
#         # subset(k + 1, n)
# subset(0, 3)  # for문이 세 번 중첩 = 3번 반복, 3단계 내려감




######
# arr = 'ABC'
# bits = []
# for i in range(2):
#     bits.append(i)
#
#     for i in range(2):
#         bits.append(i)
#
#         for i in range(2):
#             bits.append(i)
#             print(bits)
#             bits.pop()
#         bits.pop()
#     bits.pop()



########
# 부분집합 활용
# arr = 'ABC'
# bits = []
# def subset(k, n):
#     if k == n:
#         print(bits)
#     else:
#         bits.append(arr[k])
#         subset(k + 1, n)   # k번 원소를 포함한다
#         bits.pop()
#
#         subset(k+1, n)  # k번 원소를 포함하지 않음
#
# subset(0, 3)

'''
출력결과: 
['A', 'B', 'C']
['A', 'B']
['A', 'C']
['A']
['B', 'C']
['B']
['C']
[]
'''
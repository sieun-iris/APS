a = 12
b = 16

for i in range(b, (a*b)+1):
    if i % a == 0 and i % b == 0:
        print(i)
        break


# i = b  # 최대값을 i에 저장
# while(True):
#     if i % a == 0 and i % b == 0:
#         print(i)
#         break
#     i += 1


T = int(input())

result = ''
for i in range(1, T+1):
    for j in range(1, T+1):
        if j != T:
            result += j*'*'+'\n'
        else:
            result += j*'*'
    break
print(result[::-1])

T = int(input())
result = ''
for i in range(T+1):
    if T == 0:
        result += '0'
        break
    result = str(T % 2) + result
    if T == 1:
        break
    T = T//2

print(result, end="")
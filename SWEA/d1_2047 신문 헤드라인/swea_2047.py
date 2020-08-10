import sys
sys.stdin = open('input.txt', 'r')

T = list(input())

result = []
for t in T:
    if t == t.upper():
        result += t
    else:
        result += t.upper()
print(''.join(result))



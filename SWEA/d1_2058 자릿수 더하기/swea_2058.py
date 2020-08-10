import sys
# sys.stdin = open('input_data/2056.txt') 경로
sys.stdin = open('input.txt', 'r')

T = list(map(int, input()))

result = []
for t in T:
    result.append(t)

print(sum(result))

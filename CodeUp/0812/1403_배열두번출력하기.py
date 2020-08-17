import sys
sys.stdin = open("1403_input.txt", "r")

T = int(input())
test_list = list(map(int, input().split()))

result = []
for t in test_list:
    result.append(t)
    a = result * 2

for i in a:
    print(i)

# for문을 따로 안쓰고 세로로 출력하는 방법은 없을까??

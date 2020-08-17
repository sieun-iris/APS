import sys
sys.stdin = open("1402_input.txt", "r")

T = int(input())
test_list = list(map(int, input().split()))
result = test_list[::-1]

for i in result:
    print(i, end = " ")

import sys
sys.stdin = open("1754_input.txt", "r")

a, b = map(int, input().split())
if a > b:
    print(b, a)
else:
    print(a, b)
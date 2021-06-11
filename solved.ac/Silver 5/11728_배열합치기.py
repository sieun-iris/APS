import sys; sys.stdin = open("11728.txt", "r")

a, b = map(int, input().split())

list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))
check = list_a + list_b
check.sort()
final = map(str, check)
print(' '.join(final))

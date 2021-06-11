import sys; sys.stdin = open("11656.txt", "r")

S = input()
s_list = []

for i in range(len(S)):
    s_list.append(S[i:len(S)])

s_list.sort()
for i in s_list:
    print(i)

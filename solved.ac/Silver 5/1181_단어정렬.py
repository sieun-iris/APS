import sys; sys.stdin = open("1181.txt", "r")

N = int(input())
case = [input() for _ in range(N)]

check = []
words = []
for i in case:
    if i not in check:
        words.append([len(i), i])
        check.append(i)

words.sort(key=lambda x:(x[0], x[1]))
for word in words:
    print(word[1])


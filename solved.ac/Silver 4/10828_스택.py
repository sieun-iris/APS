import sys; sys.stdin = open("10828.txt", "r")

N = int(input())
case = [input() for _ in range(N)]
stack = []

for i in case:
    if i.split(' ')[0] == 'push':
        stack.append(int(i.split(' ')[1]))
    elif i.split(' ')[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif i.split(' ')[0] == 'size':
        print(len(stack))
    elif i.split(' ')[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)


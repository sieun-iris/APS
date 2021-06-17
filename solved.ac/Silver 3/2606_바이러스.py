import sys; sys.stdin = open("2606.txt", "r")

computers = int(input())
pair = int(input())
G = [[] for _ in range(computers + 1)]
visit = [False for _ in range(computers + 1)]


def DFS(num):
    S = []
    S.append(num)
    count = 0
    visit[num] = True

    while S:
        target = S.pop()
        for g in G[target]:
            if not visit[g]:
                S.append(target)
                S.append(g)
                visit[g] = True
                count += 1
                break
    print(count)


for i in range(pair):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

DFS(1)


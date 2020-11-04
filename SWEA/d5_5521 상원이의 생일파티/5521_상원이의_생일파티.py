import sys; sys.stdin = open("5521.txt", "r")
from collections import deque

def BFS(s, G):
    global visit
    Q = deque()
    Q.append(s)
    visit[s] = 0

    while Q:
        v = Q.popleft()
        for w in G[v]:
            if not visit[w]:
                visit[w] = visit[v] + 1
                Q.append(w)


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    visit = [0] * (N + 1)

    for i in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    # print(G)

    BFS(1, G)
    # print(visit)

    count = 0
    for i in range(2, len(visit)):
        if visit[i] <= 2 and visit[i] != 0:
            count += 1
    print('#{} {}'.format(t, count))












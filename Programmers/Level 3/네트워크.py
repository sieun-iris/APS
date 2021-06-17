n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
visited = [0 for _ in range(n)]


def solution(n, computers):
    answer = 0
    for i in range(n):
        if visited[i] == 0:
            DFS(i)
            answer += 1
    print(answer)


def DFS(i):
    visited[i] = 1
    for j in range(n):
        if j != i and computers[i][j] == 1 and visited[j] == 0:
            DFS(j)


solution(n, computers)

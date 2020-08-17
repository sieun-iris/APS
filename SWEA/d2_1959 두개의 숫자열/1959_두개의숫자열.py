import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    n_list = list(map(int, input().split()))
    m_list = list(map(int, input().split()))
    result = 0

    if N < M:
        for i in range(M - N + 1):
            total = 0
            for j in range(N):
                total += n_list[j] * m_list[j+i]
            if total > result:
                result = total

    else:
        for i in range(N - M):
            total = 0
            for j in range(M):
                total += n_list[j+i] * m_list[j]
            if total > result:
                result = total

    print(result)
import sys
sys.stdin = open('5102.txt')

from collections import deque

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]

    for _ in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    s, g = map(int, input().split())

    def BFS(s, g):
        visit = [0] * (V + 1)
        Q = deque()
        visit[s] = 1
        Q.append(s)

        while Q:
            v = Q.popleft()
            if v == g:
                return visit[v] - 1

            for w in G[v]:
                if not visit[w]:  #
                    visit[w] = visit[v] + 1
                    Q.append(w)
        return 0

    print(f'#{tc} {BFS(s, g)}')
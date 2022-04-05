import sys
sys.stdin = open('11902.txt')

def BFS(s, G):
    D = [0xffffff] * (N + 1)
    P = [j for j in range(N + 1)]
    D[s] = 0
    Q = [s]

    while Q:
        u = Q.pop(0)
        for v, w in G[u]:
            if D[v] > D[u] + w:
                D[v] = D[u] + w
                P[v] = u
                Q.append(v)

    return D[N]

T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split()) # N: 노드 번호, E : 간선 개수
    G = [[] for _ in range(N+1)]

    for i in range(E):
        u, v, w = map(int, input().split())
        G[u].append((v, w))

    ans = BFS(0, G)

    print(f'#{tc} {ans}')



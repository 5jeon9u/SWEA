import sys
sys.stdin = open('12398.txt')

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())  # 정점수, 간선수
    G = [[0] * (V + 1) for _ in range(V + 1)]  # 인접 행렬

    # 간선수만큼 입력 처리
    for _ in range(E):
        u, v = map(int, input().split())
        G[u][v] = G[v][u] = 1

    S, G = map(int, input().split())

    for i in range(E):
        if G[S][i] == G[i][G] == 1:
            print('f#{tc} 1')

    for lst in G[1:]:
        print(*lst[1:])

    # S, G = map(int, input().split())
    #
    # stack = []
    # print(G)
    # for i in range(E):
    #     if lst[i][0] == S:
    #         stack.append(lst[i][1])


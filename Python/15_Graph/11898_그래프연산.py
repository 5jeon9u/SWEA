import sys
sys.stdin = open('11898.txt')
from collections import deque

def operate():
    G = [0] * 1000001
    Q = deque()
    Q.append(N)
    visit[N] = 1
    while Q:
        x = Q.popleft()
        if x == M:
            return visit[M]-1
        else:
            G[x] = [x + 1, x - 1, x * 2, x - 10]
            for w in G[x]:
                if w == M:
                    return visit[x]
                elif 0 < w <= 1000000 and visit[w] == 0:
                    Q.append(w)
                    visit[w] = visit[x] + 1
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visit = [0] * 1000001
    ans = operate()
    print(f'#{tc} {ans}')
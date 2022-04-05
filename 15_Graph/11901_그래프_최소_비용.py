import sys
sys.stdin = open('11901.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    fuel = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0xffffff] * N for _ in range(N)]
    Q = [(0, 0)]
    visit[0][0] = 0
    while Q:
        r, c = Q.pop(0)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                dump = 1
                if fuel[r][c] < fuel[nr][nc]:
                    dump += fuel[nr][nc] - fuel[r][c]
                if visit[r][c] + dump < visit[nr][nc]:
                    visit[nr][nc] = visit[r][c] + dump
                    Q.append((nr, nc))
    print(f'#{tc} {visit[N-1][N-1]}')



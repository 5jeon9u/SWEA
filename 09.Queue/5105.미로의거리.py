import sys; sys.stdin = open('5105.txt', 'r')
from collections import deque

T = int(input())

for tc in range(1, T+1):

    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]

    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]

    sr = sc = er = ec = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                sr, sc = i, j
            if matrix[i][j] == 3:
                er, ec = i, j

    visit = [[0] * N for _ in range(N)]
    Q = deque()

    visit[sr][sc] = 1
    Q.append((sr, sc))

    while Q:
        r, c = Q.popleft()
        if r == er and c == ec:
            break
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 배열 범위가 아닌 경우
            if nr < 0 or nr >= N or nc < 0 or nc >= N: 
                continue
            # 벽이거나 이미 방문한 곳인 경우
            if matrix[nr][nc] == 1 or visit[nr][nc]:
                continue
            visit[nr][nc] = visit[r][c] + 1
            Q.append((nr, nc))

    if visit[er][ec]:
        visit[er][ec] -= 2
    print(f'#{tc} {visit[er][ec]}')
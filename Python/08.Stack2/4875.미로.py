import sys
sys.stdin = open('4875.txt')

# 경계를 벗어나면 안되고
# 벽이면 안되고
# 방문 한곳이면 안되고
# 위 3가지에 안걸리면 된다

def dfs(r, c):
    # 현재 위치 방문
    visited[r][c] = 1
    # 인접 정점 찾음
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        # 경계 확인
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        # 길인지 확인
        if lst[nr][nc] == '1' or visited[nr][nc] == 1: # 벽과 방문 정보
            continue
        dfs(nr, nc)

T = int(input())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T + 1):
    N = int(input())
    lst = [input() for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    val1 = val2 =  0
    er = ec =  0
    # 시작위치
    for i in range(N):
        for j in range(N):
            if lst[i][j] == '2':
                val1 = i
                val2 = j
            if lst[i][j] == '3':
                er = i
                ec = j

    dfs(val1, val2)
    print(f'#{tc} {visited[er][ec]}')









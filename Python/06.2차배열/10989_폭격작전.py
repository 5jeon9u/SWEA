import sys
sys.stdin = open('10989.txt')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split()) # 지도 크기 N, 폭탄의 수 M
    matrix = [list(map(int, input().split())) for _ in range(N)] # 배열
    info = [list(map(int, input().split())) for _ in range(M)] # 폭발 위치와 폭발력

    boom = [[0]*N for _ in range(N)] # 폭격이 발생한 위치의 값

    total = 0 # 피해 적군의 합

    dr = [0, -1, 1, 0, 0]  # 원점, 상하좌우
    dc = [0, 0, 0, 1, -1]

    for i in range(M):
        for j in range(5): #원점과 상하좌우 5방향에 대해 탐색
            r = info[i][0]
            c = info[i][1] # 폭탄 투하 위치
            nr, nc = r, c # 폭탄 투하 위치 초기화
            for k in range(info[i][2]): # 폭발력이 영향을 주는 범위만큼만 실행
                if 0 <= nr + dr[j] < N and 0 <= nc + dc[j] < N: # 해당 인덱스가 배열 내에 있는지 검색
                    nr, nc = nr + dr[j], nc + dc[j]
                    if boom[nr][nc] == 0:
                        boom[nr][nc] += matrix[nr][nc]
                        total += boom[nr][nc]

    print(f'#{tc+1} {total}')
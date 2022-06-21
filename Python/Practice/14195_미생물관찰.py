import sys
sys.stdin = open('14195.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    sample = [list(input()) for _ in range(N)]
    visit = [[0]*M for _ in range(N)]
    max_ans = 0
    A = B = 0
    Q = []
    for i in range(N):
        for j in range(M):
            # 아직 확인안한 알파벳일 경우, Q에 삽입
            if sample[i][j] != '_' and visit[i][j] == 0:
                Q.append((i, j))
                visit[i][j] = 1
                # 미생물 개체 수 확인
                if sample[i][j] == 'A':
                    A += 1 
                else:
                    B += 1
                # 개체 중 가장 큰 크기의 개체 확인
                ans = 1
                while Q:
                    r, c = Q.pop(0)
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr = r + dr
                        nc = c + dc
                        # 방문 및 범위 체크
                        if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0 and sample[r][c] == sample[nr][nc]:
                            visit[nr][nc] = 1
                            Q.append((nr,nc))
                            ans += 1

                if max_ans < ans:
                    max_ans = ans

    print(f'#{tc} {A} {B} {max_ans}')

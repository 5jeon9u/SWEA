import sys
sys.stdin = open('12712.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]

    br = [-1, -1, 1, 1]
    bc = [-1, 1, -1, 1]

    max = 0
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0

    for i in range(N):
        for j in range(N):
            cnt1 = matrix[i][j]
            cnt2 = matrix[i][j]
            for k in range(4):
                r, c = i, j
                for l in range(M-1):
                    if 0 <= r + dr[k] < N and 0 <= c + dc[k] < N:
                        r = r + dr[k]
                        c = c + dc[k]
                        cnt1 += matrix[r][c]
            for m in range(4):
                r2, c2 = i, j
                for n in range(M-1):
                    if 0 <= r2 + br[m] < N and 0 <= c2 + bc[m] < N:
                        r2 = r2 + br[m]
                        c2 = c2 + bc[m]
                        cnt2 += matrix[r2][c2]
            if cnt1 < cnt2:
                cnt3 = cnt2
            else:
                cnt3 = cnt1
            if max < cnt3:
                max= cnt3

    print(f'#{tc} {max}')




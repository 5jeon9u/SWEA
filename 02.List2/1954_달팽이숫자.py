import sys
sys.stdin = open('1954.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    # 우하좌상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    r, c = 0, 0 # 초기 위치
    dist = 0

    for n in range(1, N*N+1):
        arr[r][c] = n
        r += dr[dist]
        c += dc[dist]

        if r < 0 or c < 0 or r >= N or c >= N or arr[r][c] != 0:
            # 실행 취소
            r -= dr[dist]
            c -= dc[dist]

            dist = (dist+1) % 4

            r += dr[dist]
            c += dc[dist]

    print(f'#{tc}')
    for row in arr:
        print(*row)


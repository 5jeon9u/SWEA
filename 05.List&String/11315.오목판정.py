import sys
sys.stdin = open('11315.txt')

def solve(arr): # 행 우선순회 하다가 'o'이 나오면 오른쪽, 왼쪽, 좌하단, 우하단을 확인해야 함
    dr = [0, 1, 1, 1]
    dc = [1, 0, 1, -1]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for d in range(4):
                    r, c = i, j
                    cnt = 0
                    # 이동하면서 개수 세기
                    # r,c가 범위 안에 있어야 함
                    while 0 <= r < N and 0 <= c < N and arr[r][c] == 'o':
                        cnt += 1
                        r += dr[d]
                        c += dr[d]
                        if cnt >= 5:
                            return 'YES'
    return 'NO'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr =[input() for _ in range(N)]

    result = solve(arr)
    print(f'#{tc} {result}')
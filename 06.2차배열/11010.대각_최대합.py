import sys
sys.stdin = open('11010.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, -1, 1, 1]
    dc = [-1, 1, -1, 1]
    max = 0 # 최댓값을 저장할 변수


    for i in range(N): # 행 순회
        for j in range(N): # 열 순회
            cnt = 0  # 현재 칸에서의 합을 저장할 변수
            cnt += matrix[i][j]
            for k in range(4): # 행과 열 순회
                r, c = i, j
                while 0 <= r + dr[k] < N and 0 <= c + dc[k] < N:
                    r = r + dr[k]
                    c = c + dc[k]
                    cnt += matrix[r][c]
            if max < cnt:
                max = cnt


    print(f'#{tc} {max}')

            

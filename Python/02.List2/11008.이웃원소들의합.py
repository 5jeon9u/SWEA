import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]


    max = 0 # 최댓값을 입력할 변수
    r_idx = 0 # 최댓값의 행 인덱스를 입력할 변수
    c_idx = 0 # 최댓값의 열 인덱스를 입력할 변수
    
    di = [-1, 0, 1, 0] # 상우하좌
    dj = [0, 1, 0, -1]
    
    x = 0 # 이동시킨 행의 위치값
    y = 0 # 이동시킨 열의 위치값

    for r in range(0, N-1):
        for c in range(0, N-1):
            count = 0  # 합을 입력할 변수
            for k in range(N):
                x = r + di[k]
                y = c + dj[k]

                if 0 <= x < N and 0 <= y < N:
                    count += arr[x][y]

            #최댓값 구하기
            if max < count:
                max = count
                r_idx = r
                c_idx = c
            elif max == count:
                if r < r_idx:
                    r_idx = r
                    c_idx = c
                elif r == r_idx:
                    if c < c_idx:
                        r_idx = r
                        c_idx = c

    print(f'#{tc + 1} {r_idx} {c_idx} {max}')
            


import sys
sys.stdin = open('4836.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    color = [list(map(int, input().split())) for _ in range(N)]

    arr = [[0]*10 for _ in range(10)] #색칠할 영역
    count = 0 #보라색이 되는 영역

    for i in range(N):
        # 빨강 칠하기
        if color[i][4] == 1:
            for r in range(color[i][0], color[i][2] + 1):
                for c in range(color[i][1], color[i][3] + 1):
                    if arr[r][c] != 1:
                        arr[r][c] += 1

        # 파랑 칠하기
        elif color[i][4] == 2:
            for m in range(color[i][0], color[i][2] + 1):
                for n in range(color[i][1], color[i][3] + 1):
                    if arr[m][n] != 2:
                        arr[m][n] += 2


    for k in range(10):
        for l in range(10):
            if arr[k][l] >= 3:
                count += 1

    print(f'#{tc+1} {count}')
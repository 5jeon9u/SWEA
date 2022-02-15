import sys

sys.stdin = open('1210.txt')

for tc in range(10):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    x = 99  # 현재 행 위치
    y = 0  # 현재 열 위치

    for i in range(100):
        if ladder[x][i] == 2:
            y = i
            break

    while x > 0:
        # 좌회전
        if y > 0 and ladder[x][y - 1] == 1:
            while y > 0 and ladder[x][y - 1] != 0:
                    y -= 1
            x -= 1
        # 우회전
        elif y < 99 and ladder[x][y + 1] == 1:
            while y < 99 and ladder[x][y + 1] == 1:
                    y += 1
            x -= 1
        # 직진
        else:
            x -= 1

    print(f'#{tc + 1} {y}')

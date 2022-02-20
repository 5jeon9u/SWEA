import sys
sys.stdin = open('1974.txt')

T = int(input())

for tc in range(1, T+1):
    matrix = [list(map(int, input().split())) for _ in range(9)]

    result = 1

    for i in range(9):
        counts = [0] * 10
        for j in range(9):
            counts[matrix[i][j]] += 1 # 행 검사
        for a in range(1, 10):
            if counts[a] != 1:
                result = 0
                break

    for i in range(9):
        counts = [0] * 10
        for j in range(9):
            counts[matrix[j][i]] += 1  # 열 검사
        for a in range(1, 10):
            if counts[a] != 1:
                result = 0


    for k in range(0, 7, 3):
        for l in range(0, 7, 3):
            counts = [0] * 10
            for m in range(k, k+3):
                for n in range(l, l+3):
                    counts[matrix[m][n]] += 1

            for a in range(1, 10):
                if counts[a] != 1:
                    result = 0

    print(f'#{tc} {result}')
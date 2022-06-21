# 교착 상태 : N극 아래 부분에 S극이 있을 때
import sys
sys.stdin = open('1220.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    table =[list(map(int, input().split())) for _ in range(N)]
    prev = [0] * N
    result = 0
    for i in range(N):
        for j in range(N):
            # 세가지 경우
            if table[i][j] == 1: #N극인 경우
                prev[j] = 1
            elif table[i][j] == 2: #S극 인경우
                if prev[j] == 1:
                    result += 1
                prev[j] = 2

    print(f'#{tc} {result}')
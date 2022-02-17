import sys
sys.stdin = open('2001.txt')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    max = 0 # 최대 파리

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            count = 0  # 죽은 파리
            for k in range(i, i + M):
                for l in range(j, j + M):
                    count += lst[k][l]
            if max < count:
                max = count

    print(f'#{tc+1} {max}')
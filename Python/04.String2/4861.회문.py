import sys
sys.stdin = open('4861.txt')
# 단일 구간으로 회문 판단
# 모든 구간으로 적용
T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    word = [input() for _ in range(N)]

    # 가로 점검
    for i in range(N): # 행 우선 탐색
        for j in range(N - M + 1): # 열 탐색
            for k in range(M//2): # 회문 점검
                if word[i][k + j] == word[i][M - 1 - k + j]:
                    continue
                else:
                    break
            else:
                print(f'#{tc+1} ', end='')
                for m in range(M):
                    print(word[i][j+m], end='')
                else:
                    print()

    # 세로 점검
    for i in range(N): # 열 우선 탐색
        for j in range(N - M + 1): # 행 탐색
            for k in range(M//2): # 회문 점검
                if word[k + j][i] == word[M - 1 - k + j][i]:
                    continue
                else:
                    break
            else:
                print(f'#{tc + 1} ', end='')
                for m in range(M):
                    print(word[j+m][i], end='')
                else:
                    print()








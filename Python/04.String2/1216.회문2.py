import sys
sys.stdin = open('1216.txt')
# 함수로도 해보기
for tc in range(10):
    T = int(input())
    word = [input() for _ in range(100)]
    r_max = 0
    c_max = 0
    flag = False
    flag2 = False

    for M in range(100,0,-1): # 회문 길이
        # 가로 점검
        for i in range(100):  # 행 우선 탐색
            for j in range(100 - M + 1):  # 열 탐색
                for k in range(M // 2):  # 회문 점검
                    if word[i][k + j] == word[i][M - 1 - k + j]:
                        continue
                    else:
                        break
                else:
                    if c_max < M:
                        c_max = M
                        flag = True
            if flag:
                break

        # 세로 점검
        for i in range(100):  # 열 우선 탐색
            for j in range(100 - M + 1):  # 행 탐색
                for k in range(M // 2):  # 회문 점검
                    if word[k + j][i] == word[M - 1 - k + j][i]:
                        continue
                    else:
                        break
                else:
                    if r_max < M:
                        r_max = M
                        flag = True
            if flag:
                break

    if r_max < c_max:
        print(f'#{tc+1} {c_max}')
    else:
        print(f'#{tc + 1} {r_max}')
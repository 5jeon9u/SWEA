import sys
sys.stdin = open('4408.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input()) # 돌아가야 할 학생의 수
    word = [list(map(int,input().split())) for _ in range(N)]

    # 카운팅
    # 이동 구간 마킹 -> 겹치는 숫자만큼 시간이 걸림
    # 복도를 카운팅 배열로

    # time = 1 # 걸리는 시간
    #
    # for i in range(len(word)-1):
    #     if word[i][0] < word[i+1][0] < word[i][1]: # 출발 지점
    #         time += 1
    #     if word
    #         if word[i][0] < word[i+1][1]: # 도착지점
    #             time += 1
    # print(f'#{tc} {time}')
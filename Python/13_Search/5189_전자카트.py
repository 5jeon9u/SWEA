import sys
sys.stdin = open('5189.txt')

def DFS(x, tot, num):
    global min_ans
    if num == N-1:
        if min_ans > tot+arr[x][1]:
            min_ans = tot+arr[x][1]

    for i in range(2, N+1): # 나머지 행을 방문
        if visit[i] == 0: # 해당 행을 방문하지 않았다면
            visit[i] = 1 # 다음 출발
            DFS(i, tot+arr[x][i], num+1)
            visit[i] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * (N+2)] \
          + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] \
          + [[0] * (N+2)]

    visit = [0] * (N+1)
    visit[1] = 1 # 첫번째 행은 고정된 출발지
    min_ans = 0Xfffffff
    ans = 0
    cnt = 0
    DFS(1, ans, cnt)
    print(f'#{tc} {min_ans}')
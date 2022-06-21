import sys
sys.stdin = open('11897.txt')

def dfs(k, cost):
    global min_cost
    if cost > min_cost:
        return

    if k == N:
        if cost <= min_cost:
            min_cost = cost
        return

    for i in range(N):
        if not factory[i]:
            factory[i] = True
            dfs(k+1, cost + arr[k][i])
            factory[i] = False

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    factory = [False] * N
    min_cost = 0xffffff
    dfs(0, 0)
    print(f'#{tc} {min_cost}')
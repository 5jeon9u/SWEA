def count_arr(N):
    ret = 0
    for i in range(N):
        cnt = 0
        for j in range(N + 1):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    ret += 1
                cnt = 0
    return ret

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] # 행방향 0추가
    arr.append([0]* N+1) # 열방향 0추가

    sol = count_arr(N)
    arr = list(map(list, zip(*arr))) # 전치행렬
    sol += count_arr(N)
    print(f'#{tc} {sol}')
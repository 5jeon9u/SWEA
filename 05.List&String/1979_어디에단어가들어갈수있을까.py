import sys
sys.stdin = open('1979.txt')

def count_arr(N):
    ret = 0 # K길이의 단어가 들어가는 칸 수
    for i in range(N+1):
        cnt = 0
        for j in range(N + 1):
            if arr[i][j] == 1:
                cnt += 1 # 입력 가능 글자수
            else:
                if cnt == K:
                    ret += 1
                cnt = 0
    return ret

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] # 열 추가
    arr.append([0] * (N+1)) # 행 추가

    sol = count_arr(N) # 행 기준 순회
    arr = list(map(list, zip(*arr))) # 전치행렬
    sol += count_arr(N) # 열 기준 순회
    print(f'#{tc} {sol}')
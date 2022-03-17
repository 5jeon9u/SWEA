import sys
sys.stdin = open('2814.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0 # 경우의 수

    for subset in range(1<<N):
        total = 0 # 합을 저장할 변수
        for i in range(N):
            if subset & (1<<i):
                total += lst[i]
        if total == K:
            cnt += 1

    print(f'#{tc} {cnt}')


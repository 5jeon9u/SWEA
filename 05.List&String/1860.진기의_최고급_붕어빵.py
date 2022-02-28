import sys
sys.stdin = open('1860.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    guest = list(map(int, input().split()))
    sec = 0
    bread = 0
    result = 'Possible'

    for i in range(N):
        sec += M 
        bread += K
        if bread == 0: # 빵이 0개이면 더이상 빵을 팔 수 없다
            result = 'Impossible'
            break
        if M < guest[i] <= sec:
            bread -= 1
        else:
            result = 'Impossible'
            break

    print(f'#{tc} {result}')
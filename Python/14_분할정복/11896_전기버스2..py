import sys
sys.stdin = open('11896.txt')


# 남아있는 배터리 양, 현재 버스 정류장, 방문 횟수
def check(charge, bus, cnt):
    global min_check
    if min_check <= cnt:
        return
    if charge == 0:
        return
    if bus == station[0]-1:
        if cnt < min_check:
            min_check = cnt
        return

    check(charge-1, bus+1, cnt)
    check(station[bus+1], bus+1, cnt + 1)

T = int(input())
for tc in range(1, T + 1):
    station = list(map(int, input().split()))
    min_check = station[0]
    check(station[1], 1, 0)
    print(f'#{tc} {min_check}')



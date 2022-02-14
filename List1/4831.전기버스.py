import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(T):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    '''
    K(이동 가능한 정류장 수)값 내에 정류소가 2개 있는 경우 큰 값을 취하고
    1개가 있는 경우 해당 값을 취하고
    종점에 도착하기 전, 범위내에 정류소가 없는 경우 0을 출력
    버스 위치가 이동할 때마다 변하는 점에 유의
    '''

    battery = [0] * (N+1) # 전기차 충전소 리스트
    for j in range(0, len(arr)):
        battery[arr[j]] = 1

    charge = 0 # 충전 횟수
    bus = 0 # 버스의 위치
    move = 0 # 이동 거리

    while bus <= N:
        count = 0  # 이동 가능 범위 내 충전 가능 횟수

        if bus + K >= N: # 버스가 현재 이동 가능 범위 내에서 종점에 도착 가능 한 경우
            print(f'#{tc + 1} {charge}')
            break

        for m in range(1, K+1): # 이동 가능 범위 내 충전소 확인
            if battery[bus+m] == 1:
                count += 1
                move = m

        if count > 0: # 이동 가능 범위 중 충전소가 있는 경우
            charge += 1 # 충전
            bus = bus + move
        else: # 이동 가능 범위 중 충전소가 없는 경우
            print(f'#{tc + 1} 0')
            break
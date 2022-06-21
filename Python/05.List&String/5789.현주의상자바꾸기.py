import sys
sys.stdin = open('5789.txt')

T = int(input())

for tc in range(T):
    N, Q = map(int, input().split()) # 상자의 수 : N, 반복 횟수 : Q

    box = [0] * N # N개의 상자 생성

    for i in range(1, Q+1): # Q횟수를 반복해서 진행
        L, R = map(int, input().split())

        for k in range(L-1, R): # L과 R범위를 정하여 상자의 값을 i를 입력
            box[k] = i

    print(f'#{tc+1}', *box)

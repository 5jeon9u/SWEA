import sys
sys.stdin = open('2817.txt')

def nCr(k, n, tot): # k부터 시작해서 n개 까지 선택
    global cnt
    if k == n:
        S = 0
        for i in range(n):
            if bits[i]:
                S += arr[i]
        if S == tot: # 부분집합의 합이 tot(K)와 같다면
            cnt += 1

    else:
        bits[k] = 0 # 현재 위치의 비트를 부분집합에 포함하지 않는 경우
        nCr(k + 1, n, tot)
        bits[k] = 1 # 현재 위치의 비트를 부분집합에 포함하는 경우
        nCr(k + 1, n, tot)

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split()) # 원소의 개수 N, 합계 K
    arr = list(map(int, input().split()))
    bits = [0] * N
    cnt = 0 # 부분 수열의 합이

    nCr(0, N, K)
    print(f'#{tc} {cnt}')
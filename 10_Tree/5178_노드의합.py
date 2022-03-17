import sys
sys.stdin = open('5178.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())

    H = [0] * (N+1)

    for i in range(M):
        key, val = map(int, input().split())
        H[key] = val

    for j in range(len(H)-1, 0, -1):
        if H[j] != 0:
            continue
        else:
            if (j*2+1) > N:
                H[j] = H[j*2]
            else:
                H[j] = H[j * 2] + H[j * 2 + 1]

    print(f'#{tc} {H[L]}')

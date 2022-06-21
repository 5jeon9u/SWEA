import sys
sys.stdin = open('11893.txt')

def BS(A, l, r, key):
    global check
    if l > r:
        return 0
    else:
        middle = (l + r) // 2
        if key == A[middle]:
            return 1
        elif key < A[middle]:
            if check == -1:
                return 0
            check = -1
            return BS(A, l, middle - 1, key)
        elif key > A[middle]:
            if check == 1:
                return 0
            check = 1
            return BS(A, middle+1, r, key)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))

    ans = 0

    for i in range(M):
        check = 0
        ans += BS(A, 0, N-1, B[i])

    print(f'#{tc} {ans}')

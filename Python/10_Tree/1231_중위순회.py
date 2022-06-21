import sys
sys.stdin = open('1231.txt')

def inorder(v):
    if v == 0:
        return
    inorder(L[v])
    print(P[v], end='')
    inorder(R[v])

for tc in range(1, 11):
    N = int(input()) # 정점의 수

    L = [0] * (N + 1)
    R = [0] * (N + 1)
    P = [0] * (N + 1)

    for i in range(1, N+1):
        arr = list(input().split())
        lst = [0] * 4

        for j in range(len(arr)):
            lst[j] = arr[j]

        L[i] = int(lst[2])
        R[i] = int(lst[3])
        P[i] = lst[1]

    print(f'#{tc}', end=' ')
    inorder(1)
    print()

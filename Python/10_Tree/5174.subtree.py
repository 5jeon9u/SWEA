import sys
sys.stdin = open('5174.txt')

def inorder(v):
    global cnt

    if v == 0:
        return
    inorder(L[v])
    cnt += 1
    inorder(R[v])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    V = E + 1

    L = [0] * (V + 1)
    R = [0] * (V + 1)
    P = [0] * (V + 1)

    cnt = 0

    for i in range(0, E*2, 2):
        p, c = lst[i], lst[i+1]
        if L[p] == 0:
            L[p] = c
        else:
            R[p] = c
        P[c] = p


    inorder(N)
    print(f'#{tc} {cnt}')

import sys
sys.stdin = open('5176.txt')

def inorder(v):
    global cnt
    if v > N:
        return
    inorder(v*2)
    C[v] = cnt
    cnt += 1
    inorder(v*2+1)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cnt = 1
    C = [0] * (N + 1)

    inorder(1)

    print(f'#{tc} {C[1]} {C[N//2]}')

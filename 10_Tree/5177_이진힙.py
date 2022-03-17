import sys
sys.stdin = open('5177.txt')

def push(item):
    global hsize
    hsize += 1
    H[hsize] = item

    c = hsize
    p = hsize // 2

    while p and H[p] > H[c]:
        H[p], H[c] = H[c], H[p]
        c = p
        p = c // 2

T = int(input())

for tc in range(1, T+1):
    H = [0] * 501
    hsize = 0

    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0

    for i in lst:
        push(i)

    while N != 0:
        cnt += H[N // 2]
        N = N // 2

    print(f'#{tc} {cnt}')
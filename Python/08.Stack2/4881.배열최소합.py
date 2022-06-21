# 열 값의 순열
# (0, ㅌ), (1, y) (2, z)
# 열 인덱스가 달라야한다

import sys
sys.stdin=open('4881.txt')

def perm(k, cur_sum):
    global ans
    if cur_sum >= ans:
        return
    if k == N:
        if ans > cur_sum:
            ans = cur_sum
    else:
        for i in range(k, N):
            cols[k], cols[i] = cols[i], cols[k]
            perm(k + 1, cur_sum + arr[k][cols[k]])  # arr[k][cols[k]]
            cols[k], cols[i] = cols[i], cols[k]

T = int(input())
for tc in range(1 ,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cols = [i for i in range(N)]
    ans = 999999999999
    perm(0, 0)
    print(f'#{tc} {ans}')







import sys
sys.stdin = open('11899.txt')

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    pick = list(map(int, input().split()))
    ans = N

    p = [i for i in range(N+1)] # 자기 자신을 루트로 하는 집합 생성

    for j in range(0, M * 2, 2):
        u = pick[j]
        v = pick[j+1]
        # u와 v의 속한 트리의 루트를 확인
        r1 = find_set(u)
        r2 = find_set(v)

        if r1 != r2:
            p[r2] = r1
            ans -= 1

    print(f'#{tc} {ans}')
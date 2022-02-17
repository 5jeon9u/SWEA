import sys
sys.stdin = open('3143.txt')

T = int(input())

for tc in range(T):
    t, p = input().split()

    n, m = len(t), len(p)
    cnt = min_count = 0
    i = 0

    while i < n - m + 1:
        for j in range(m):
            if p[j] == t[i + j]:
                continue
            else:
                i += 1
                break
        else:
            i += m
            cnt += 1

    min_count = n - (cnt * (m-1))

    print(f'#{tc+1} {min_count}')
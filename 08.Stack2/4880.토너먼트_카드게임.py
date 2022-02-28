import sys
sys.stdin = open('4880.txt')


def game(s, e):
    if s == e:
        return s
    else:
        mid = (s + e) // 2
        l = game(s, mid)
        r = game(mid + 1, e)

        m = lst[l]
        n = lst[r]

        if (m + n) % 2:
            return r if m < n else l
        else:
            return l if m <= n else r


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst = [0] + list(map(int, input().split()))
    print(f'#{tc} {game(1, N)}')






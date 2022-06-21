import sys
sys.stdin = open('4864.txt')

T = int(input())

for tc in range(T):
    p = input()
    t = input()

    n, m = len(t), len(p)

    for i in range(n - m + 1):
        for j in range(m):
            if p[j] != t[i + j]:
                break
        else:
            print(f'#{tc+1} 1')
            break
    else:
        print(f'#{tc + 1} 0')
import sys
sys.stdin = open('9367.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    C = list(map(int, input().split()))

    max_count = 1
    now_count = 1

    for i in range(N-1):
        if C[i] < C[i+1]:
            now_count += 1
            if now_count > max_count:
                max_count = now_count
        else:
            now_count = 1

    print(f'#{tc + 1} {max_count}')
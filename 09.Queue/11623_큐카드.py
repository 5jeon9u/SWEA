import sys
sys.stdin = open('11623.txt')

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    cheeze = list(map(int, input().split()))

    oven = [0]
    for i in range(N):
        oven.append(i)
    f, r = 0, N
    next_pizza = N
    while ((f + 1) % (N + 1)) != r:
        f = (f + 1) % (N + 1)
        num = oven[f]
        cheeze[num] //= 2

        if cheeze[num]:
            r = (r + 1) % (N + 1)
            oven[r] = num
        else:
            if next_pizza < M:
                r = (r + 1) % (N + 1)
                oven[r] = next_pizza
                next_pizza += 1

    print(f'#{tc} {oven[r] + 1}')

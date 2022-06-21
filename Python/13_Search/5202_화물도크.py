import sys
sys.stdin = open('5202.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    check = []
    for _ in range(N):
        check.append(list(map(int, input().split())))

    check.sort(key=lambda x : x[1])

    ft = check[0][1]
    ans = 1
    for i in range(1,N):
        if ft <= check[i][0]:
            ans += 1
            ft = check[i][1]

    print(f'#{tc} {ans}')
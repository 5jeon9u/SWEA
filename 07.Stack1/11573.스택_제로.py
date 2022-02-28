import sys
sys.stdin = open('11573.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    stack = []
    cnt = 0

    for i in range(N):
        if lst[i] != 0:
            stack.append(lst[i])
        else:
            stack.pop()

    for j in range(len(stack)):
        cnt += stack[j]

    print(f'#{tc} {cnt}')






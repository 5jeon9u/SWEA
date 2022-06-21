import sys
sys.stdin = open('5201.txt')

T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    container.sort(reverse=True)
    truck.sort(reverse=True)

    i = j = 0
    ans = 0

    while i < len(truck) and j < len(container):
        if truck[i] >= container[j]:
            ans += container[j]
            i += 1
            j += 1
        else:
            j += 1

    print(f'#{tc} {ans}')

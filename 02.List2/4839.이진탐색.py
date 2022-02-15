# 중간위치값이 배제되지 않고 있다.
import sys
sys.stdin = open('4839.txt')

T = int(input())

for tc in range(T):
    P, A, B = map(int, input().split())

    start = 1
    end = P
    A_count = 0 # A의 이진 탐색 횟수

    while start <= end:
        middle = (start + end) // 2

        if middle == A:
            break
        elif middle < A:
            start = middle
            A_count += 1
        else:
            end = middle
            A_count += 1

    start = 1
    end = P
    B_count = 0  # B의 이진 탐색 횟수
    while start <= end:
        middle = (start + end) // 2

        if middle == B:
            break
        elif middle < B:
            start = middle
            B_count += 1
        else:
            end = middle
            B_count += 1

    if A_count > B_count:
        print(f'#{tc+1} B')
    elif A_count < B_count:
        print(f'#{tc+1} A')
    else:
        print(f'#{tc+1} 0')
# 선택 정렬
import sys
sys.stdin = open('4843.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(0, 9, 2):
        max_idx = i
        min_idx = i + 1
        for j in range(i+1, N):
            if arr[max_idx] < arr[j]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]

        for l in range(i+2, N):
            if arr[min_idx] > arr[l]:
                min_idx = l
        arr[i+1], arr[min_idx] = arr[min_idx], arr[i+1]

    print(f'#{tc+1}', *arr[0:10])



import sys
sys.stdin = open('5208.txt')

def merge_sort(s, e):
    global cnt

    if s == e:
        return
    mid = (s + e - 1) // 2
    merge_sort(s, mid)
    merge_sort(mid + 1, e)

    if arr[mid] > arr[e]:
        cnt += 1

    i, j, k = s, mid + 1, s
    # 현재 인덱스 범위 내 두 시작 값을 가장 먼저 비교
    # 정렬하려는 범위의 시작 값 중 작은 값을 맨 앞으로 이동
    while i <= mid and j <= e:
        # 두 값 중 하나씩 비교하면서 앞에서부터 정렬
        # 정렬된 인덱스 범위의 인덱스 값을 1씩 증가시키면서, 해당 인덱스 범위의 값들이 모두 정렬이 완료 된 경우
        if arr[i] < arr[j]:
            tmp[k] = arr[i]; k, i = k + 1, i + 1
        else:
            tmp[k] = arr[j]; k, j = k + 1, j + 1
    # 남은 범위의 값들을 뒷부분에 병합시킴
    while i <= mid:
        tmp[k] = arr[i]; k, i = k + 1, i + 1
        # 만약 맨 뒷부분에 있는 영역이 가장 작은 값으로 맨 앞에 이동하게 된다면 그 뒤는 뒤따라 온다..?
    while j <= e:
        tmp[k] = arr[j]; k, j = k + 1, j + 1

    # tmp ==> arr 복사
    for i in range(s, e + 1):
        arr[i] = tmp[i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    tmp = [0] * N
    cnt = 0
    merge_sort(0, N - 1)
    print(f'#{tc} {arr[N//2]} {cnt}')
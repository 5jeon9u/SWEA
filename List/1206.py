import sys
sys.stdin = open('input.txt')

for tc in range(10):
    N = int(input())
    arr = list(map(int, input().split()))

    count = 0
    for i in range(2, N-2):
        new_lst = [arr[i-2], arr[i-1], arr[i+1], arr[i+2]] # 기준 값의 좌우 2칸의 값을 리스트로 생성

        max = 0
        for j in range(len(new_lst)): # 해당 리스트에서 최댓값을 변수 max에 저장
            if max < new_lst[j]:
                max = new_lst[j]

        if max < arr[i]: # 리스트의 최댓값보다 기준값이 더 높을 경우, 그 차이를 누적하여 변수 count에 저장
            count += arr[i] - max

    print(f'#{tc + 1} {count}')


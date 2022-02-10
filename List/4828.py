import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    num = 0 # 차이 값을 저장할 변수
    min = arr[0] # 최소값을 저장할 변수
    max = arr[0] # 최대값을 저장할 변수

    for i in range(len(arr)):
        if max < arr[i]:
            max = arr[i]
        if min > arr[i]:
            min = arr[i]

    print(f'#{tc + 1} {max-min}')


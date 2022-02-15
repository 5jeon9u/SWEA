# 이전 구간합의 맨 앞을 제거하고 맨 뒤를 더해주는 방식으로도 할 수 있다.

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    sum_list = [] #M개의 합들을 저장할 리스트

    for i in range(0, N-M+1):
        count = 0  # M개의 합을 저장할 변수
        for j in range(0, M):
            count += arr[i+j]
        sum_list.append(count)

    max = min = sum_list[0]

    # 리스트에 넣는 것보다 바로바로 비교하는게 훨씬 좋음
    for k in range(0, len(sum_list)):
        if max < sum_list[k]:
            max = sum_list[k]
        if min > sum_list[k]:
            min = sum_list[k]

    print(f'#{tc+1} {max-min}')



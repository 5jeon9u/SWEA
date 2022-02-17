import sys
sys.stdin = open('9386.txt')

T = int(input())

# (1)
for tc in range(T):
    N = int(input())
    arr = list(map(int, input()))

    count = 0
    max = 0

    # 경계값유의
    for i in range(len(arr)):
        if arr[i] == 1:
            count += 1
        else:
            if max < count:
                max = count
            count = 0
    #(1)
    if max < count:
        max = count
    #(2) 끝자리에 0을 추가하여 반복
    print(f'#{tc+1} {max}')

# (2)
# for tc in range(1, T + 1):
#     N = int(input())
#     d = input().split('0')
#     m = 0
#     for data in d:
#         if len(data) > m:
#             m = len(data)
#     print('#{} {}'.format(tc,m))
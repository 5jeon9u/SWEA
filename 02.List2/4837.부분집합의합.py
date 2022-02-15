import sys
sys.stdin = open('4837.txt')

T = int(input())

for tc in range(T):
    N, K = map(int, input().split())

    arr = []
    total_count = 0  # N과 K 조건이 모두 일치하는 부분집합의 수

    for i in range(1, 13):
        arr.append(i)

    for subset in range(1 << 12):
        sum = 0  # 부분집합의 합
        count = 0  # 부분집합의 원소의 수
        for j in range(12):
            if subset & (1 << j):
                sum += arr[j]
                count += 1

        if count == N and sum == K:
            total_count += 1

    print(f'#{tc+1} {total_count}')
                
import sys
sys.stdin = open('1952.txt')

T = int(input())

for tc in range(1, T+1):
    day, month, three, year = map(int, input().split())
    plan = [0] + list(map(int, input().split()))

    # 각 달의 누적 값을 저장할 리스트
    memo = [year] * 13 # 최솟값을 찾는 것이므로 가질 수 있는 최댓값으로 설정
    memo[0] = 0 # 12개월에서 제외

    for n in range(1, 13):
        a = b = c = year # 가질 수 있는 값 중 가장 큰 값으로 설정
        if n >= 1: # 가능한 배열 범위를 위한 설정
            a = memo[n-1] + plan[n] * day
            b = memo[n-1] + month
        if n >= 3: # 가능한 배열 범위를 위한 설정
            c = memo[n-3] + three
        memo[n] = min(memo[n], a, b, c)

    print(f'#{tc} {min(year, memo[12])}')








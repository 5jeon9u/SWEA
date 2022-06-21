import sys
sys.stdin = open('11892.txt')

# Hoare

def Quick(begin, end):
    if begin >= end: # 정렬할 영역이 없음
        return

    # pivot = (begin + end) // 2
    L = begin
    R = end

    while L < R : # 두 부분이 만나지 않았으므로 계속 이동
        while L <= end and lst[L] <= lst[begin]: # 왼쪽 부분에서 피봇보다 큰 부분을 만나면 멈춤 = 피봇 기준으로 왼쪽에 작은 값을 정렬해야 하므로 큰 값을 찾아야함
            L += 1
        while lst[R] > lst[begin]: # 오른쪽 부분에서 피봇보다 작은 부분을 만나면 멈춤 = 피봇 기준으로 오른쪽에 큰 값을 정렬해야 하므로 작은 값을 찾아야함
            R -= 1
        if L < R:
            lst[L], lst[R] = lst[R], lst[L] # 피봇을 기준으로 좌측과 우측에 조건이 맞지 않는 부분들을 정렬
    # 두 부분이 만나게 되면 피봇을 재설정해줌
    lst[begin], lst[R] = lst[R], lst[begin]

    Quick(begin, R-1)
    Quick(R + 1, end)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    Quick(0, N-1)
    print(f'#{tc} {lst[N//2]}')



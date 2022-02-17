import sys
sys.stdin = open('5432.txt')

T = int(input())
for tc in range(1, T + 1):
    S = input()
    d = 2  # 열린 다음 바로 닫는 것이 들어왔을 때, 2는 의미없는 숫자
    st = 0
    count = 0

    for i in S:
        if i == '(':
            st += 1
            d = 1
        elif i == ')':
            st -= 1
            if d == 1:
                count += st
            elif d == 0:
                count += 1
            d = 0
    print(f'#{tc} {count}')
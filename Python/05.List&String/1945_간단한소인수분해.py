# 나누어 떨어지면 해당 소수가 있는 것
# 카운트 배열과 유사
import sys
sys.stdin = open('1945.txt')

N = int(input())

for tc in range(1, N+1):
    num = int(input())

    lst = [2, 3, 5, 7, 11]
    cnt = [0] * 5

    for i in range(0, 5):
        while num % lst[i] == 0:
            cnt[i] += 1
            num = num // lst[i]

    print(f'#{tc}', *cnt)

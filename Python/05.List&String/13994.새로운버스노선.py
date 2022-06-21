import sys
sys.stdin = open('13994.txt')

T = int(input())

for tc in range(1, T+1):
    max = 0
    N = int(input()) # 노선의 수
    lst = [0] * 1001
    for i in range(N):
        bus, A, B = map(int, input().split())
        lst[A] += 1
        lst[B] += 1
        if bus == 1:
            for j in range(A+1, B):
                lst[j] += 1
        elif bus == 2:
            if A % 2: # 홀수
                for l in range(A+1, B):
                    if l % 2:
                        lst[l] += 1
            else: # 짝수
                for k in range(A+1, B):
                    if k % 2 == 0:
                        lst[k] += 1
        elif bus == 3:
            if A % 2:  # 홀수
                for m in range(A+1, B):
                    if m % 3 == 0 and m % 10 != 0:
                        lst[m] += 1
            else:  # 짝수
                for n in range(A+1, B):
                    if n % 4 == 0:
                        lst[n] += 1

    for p in range(len(lst)):
        if max < lst[p]:
            max = lst[p]

    print(f'#{tc} {max}')



# 딕셔너리 응용

import sys
sys.stdin = open('4865.txt')

T = int(input())

for tc in range(T):
    p = input()
    t = input()

    max_count = 0

    n, m = len(t), len(p)

    for i in range(m): #패턴
        count = 0
        for j in range(n): #텍스트
            if p[i] == t[j]:
                count += 1

        if max_count < count:
            max_count = count

    print(f'#{tc + 1} {max_count}')
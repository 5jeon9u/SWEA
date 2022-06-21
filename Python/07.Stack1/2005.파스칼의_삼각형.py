# 조합을 구하는 Memoization 문제
# 조합의 재귀적 정의(nCr = n-1Cr-1 + n-1Cr)
# 재귀적 사례 n = r or r = 0, 1
# n과 r이 문제의 크기(식별/구분)를 나타내는 값

# 02/22 메모제이션으로 풀어보기(교수님 답안과 비교)
import sys
sys.stdin = open('2005.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    pascal = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == j or j == 0:
                pascal[i][j] = 1
            if i > j:
                pascal[i][j] = pascal[i-1][j] + pascal[i-1][j-1]

    print(f'#{tc}')

    for i in range(N):
        for j in range(N):
            if i >= j:
                print(pascal[i][j], end=' ')
        print()
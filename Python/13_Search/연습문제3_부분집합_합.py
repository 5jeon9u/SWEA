def nCr(k, n, tot): # k부터 시작해서 n개 까지 선택
    global cnt
    if k == n:
        S = 0
        for i in range(n):
            if bits[i]:
                S += arr[i]
        if S == tot: # 부분집합의 합이 tot(K)와 같다면
            print('[', end='')
            for j in range(n):
                if bits[j]:
                    print(f'{arr[j]}', end=' ')
            print(']')

    else:
        bits[k] = 0 # 현재 위치의 비트를 부분집합에 포함하지 않는 경우
        nCr(k + 1, n, tot)
        bits[k] = 1 # 현재 위치의 비트를 부분집합에 포함하는 경우
        nCr(k + 1, n, tot)

N, K = 10, 0 # 원소의 개수 N, 합계 K
arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
bits = [0] * N

nCr(0, N, K)

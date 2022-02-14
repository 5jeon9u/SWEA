import sys
sys.stdin = open('1209.txt')

for tc in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    sum_lst = [] # 각 합을 구해 저장할 리스트

    # 행과 열의 합 구하기
    for i in range(0, 100):
        r_count = 0  # 행의 합을 구해 저장할 변수
        l_count = 0  # 열의 합을 구해 저장할 변수
        for j in range(0, 100):
            r_count += arr[i][j]
            l_count += arr[j][i]
        sum_lst.append(r_count)
        sum_lst.append(l_count)

    m_count = 0  # 좌상단에서 시작하는 대각선의 합을 구해 저장할 변수
    n_count = 0  # 우상단에서 시작하는 대각선의 합을 구해 저장할 변수

    # 대각선의 합 구하기
    for m in range(0, 100):
        for n in range(0, 100):
            if m == n:
                m_count += arr[m][n]
                n_count += arr[m][100-1-n]
    sum_lst.append(m_count)
    sum_lst.append(n_count)

    max = 0 # 최댓값을 저장할 변수

    for k in range(0, len(sum_lst)):
        if max < sum_lst[k]:
            max = sum_lst[k]

    print(f'#{N} {max}')


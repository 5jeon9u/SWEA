import sys
sys.stdin = open('1209.txt')

for tc in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    print(arr)
    # arr = []
    # for _ in range(100):
    #   arr.arrpend(list(map(int, input().split()))

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
    # 10000번을 반복하는 것
    # 굳이 읽지 않아도 될 코드를 읽어버림
    for m in range(0, 100):
        for n in range(0, 100):
            if m == n:
                m_count += arr[m][n]
                n_count += arr[m][100-1-n]
    sum_lst.append(m_count)
    sum_lst.append(n_count)

    # 리스트에 넣는 것보다 바로바로 비교하는게 훨씬 좋음
    max = 0 # 최댓값을 저장할 변수

    for k in range(0, len(sum_lst)):
        if max < sum_lst[k]:
            max = sum_lst[k]

    print(f'#{N} {max}')


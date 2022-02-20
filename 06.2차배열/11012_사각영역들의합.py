import sys
sys.stdin = open('11012.txt')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)] # 배열
    info = [list(map(int, input().split())) for _ in range(M)] # 사각형 정보

    count = 0 # 영역의 총 합
    b_lst = [] # 좌표 값 리스트를 저장할 리스트

    for i in range(M): # 사각형의 개수 만큼 순회
        for j in range(info[i][2]): # 행의 길이
            for k in range(info[i][2]): # 열의 길이
                a_lst = []  # 좌표 값을 저장할 리스트
                if 0 <= info[i][0] + j < N and 0 <= info[i][1] + k < N: # 벗어나는 영역 처리
                    a_lst.append(info[i][0] + j)
                    a_lst.append(info[i][1] + k)
                    if a_lst not in b_lst:
                        b_lst.append(a_lst)
                        count += matrix[info[i][0] + j][info[i][1] + k] # 영역의 합 구하기

    print(f'#{tc+1} {count}')
import sys
sys.stdin = open('2819.txt')

def dfs(n, ci, cj, num): # 매개변수로 선택한 개수 n을 전달
    # 7개의 숫자가 선택되면 종료됨
    if n == 7:
        sset.add(num) # 중복을 제거하기 위해 set에 대입
        return
    # 4방향 호출
    for di, dj in ((-1,0), (1, 0), (0, -1), (0, 1)):
        ni, nj = ci+di, cj+dj
        # 범위 확인
        if 0 <= ni < 4 and 0 <= nj < 4:
            dfs(n+1, ni, nj, num+str(arr[ni][nj]))
    return


T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]

    sset = set() # 중복 제거를 위한 set
    
    # 좌표 탐색
    for i in range(4):
        for j in range(4):
            dfs(0, i, j, '') # 선택 개수, 시작 행, 시작 열, 만든 수

    print(f'#{tc} {len(sset)}')










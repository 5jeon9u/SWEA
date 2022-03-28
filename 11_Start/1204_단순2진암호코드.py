import sys
sys.stdin = open('1204.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 암호 배열
    arr = [input() for _ in range(N)]
    
    # [1] 암호 코드 위치 찾기
    x = y = 0
    for i in range(N):
        for j in range(M):
            if arr[i][M-1-j] == '1':
                # 암호 코드의 시작 좌표 저장
                x = i
                y = M-1-j
                break

    # [2] 암호 리스트 생성
    lst = arr[x][y-55:y+1]

    # [3] 암호 정보 추출
    pwd = {'0001101' : 0, '0011001' : 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
    output = [0]
    for m in range(0, len(lst), 7):
        output.append((pwd.get(lst[m:m+7])))

    # [4] 암호 검증
    odd = even = total = 0
    for k in range(1, 8):
        if k % 2:
            odd += output[k]
        else:
            even += output[k]

    total = (odd*3) + (even) + output[8]

    # [5] 올바른 암호일 경우 출력값
    ans = 0
    for l in range(len(output)):
        ans += output[l]

    # [6] 암호 검증 후 출력
    if total % 10 == 0:
        print(f'#{tc} {ans}')
    else:
        print(f'#{tc} 0')











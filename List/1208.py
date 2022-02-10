import sys
sys.stdin = open('sample_input.txt')

T = 10
for tc in range(T):
    D = int(input())
    box = list(map(int, input().split()))

    while D >= 0: # 덤프 횟수 이내 덤프 진행
        max = min = box[0]  # 최고점과 최저점
        max_idx = min_idx = 0  # 최고점과 최저점의 위치

        for i in range(1, len(box)): # 현재 박스들의 , 그리고 그 위치를 구함
            if max < box[i]:
                max = box[i]
                max_idx = i
            if min > box[i]:
                min = box[i]
                min_idx = i

        if max - min <= 1: # 그 차이값이 1이내일 경우
            print(f'#{tc+1} {max-min}') # 평단화 작업 완료
            break
        else: # 차이값이 1을 초과 할 경우 평단화 작업을 진행
            box[max_idx] -= 1
            box[min_idx] += 1
            D -= 1

    print(f'#{tc + 1} {max - min}')
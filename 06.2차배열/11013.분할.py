import sys
sys.stdin = open('11013.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    ret = 100 # 최소 차이
    for i in range(N-1):
        cnt1 = 0
        for j in range(i+1): # 첫번째 구간 합 시작
            cnt1 += lst[j]
        for k in range(j+1, N-1): # 첫번째 구간이 정해진 다음 부터 두번째 구간을 정함
            cnt2 = 0
            max = 0
            min = 0
            for l in range(j+1, k+1):
                cnt2 += lst[l]
                if cnt1 < cnt2:
                    max, min = cnt2, cnt1
                else:
                    max, min = cnt1, cnt2
                cnt3 = 0
                for p in range(l+1, N):
                    cnt3 += lst[p]
                if max < cnt3:
                    max = cnt3
                if min > cnt3:
                    min = cnt3
                new = max - min
                if new < ret:
                    ret = new

    print(f'#{tc} {ret}')





            

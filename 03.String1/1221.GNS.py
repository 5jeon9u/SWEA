# 카운팅 정렬로도 풀어보기
import sys
sys.stdin = open('1221.txt')

T = int(input())

for i in range(T):
    case, N = input().split()
    lst = list(map(str, input().split()))

    num_dict = {'ZRO' : 0, 'ONE' : 1, 'TWO' : 2, 'THR' : 3, 'FOR' : 4, 'FIV' : 5, 'SIX' : 6, 'SVN' : 7, 'EGT' : 8, 'NIN' : 9}

    N = int(N)

    for j in range(N-1):
        min = j
        for k in range(j+1, N):
            if num_dict.get(lst[min]) > num_dict.get(lst[k]):
                min = k

        lst[j], lst[min] = lst[min], lst[j]

    print(f'{case}', *lst)

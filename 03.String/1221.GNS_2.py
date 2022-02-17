# 정수로 변환 후 카운팅 정렬하는 것이 가장 효과적
import sys
sys.stdin = open('1221.txt')

T = int(input())

for i in range(T):
    case, N = input().split()
    lst = list(map(str, input().split())) # input().split()

    num_dict = {'ZRO' : 0, 'ONE' : 1, 'TWO' : 2, 'THR' : 3, 'FOR' : 4, 'FIV' : 5, 'SIX' : 6, 'SVN' : 7, 'EGT' : 8, 'NIN' : 9}

    N = int(N)

    C = [0] * 10 # 카운트 배열
    B = [0] * len(lst) # 정렬된 배열

    for j in range(0, len(lst)):
        C[num_dict.get(lst[j])] += 1

    for l in range(1, len(C)):
        C[l] += C[l-1]

    for k in range(len(B)-1, -1, -1):
        C[num_dict.get(lst[k])] -= 1
        B[C[num_dict.get(lst[k])]] = lst[k]

    print(f'{case}', *B)

# 꼼수
#
# A = [0, 4, 1, 3, 1, 2, 4, 1,]
# K = 4
# C = [0] * (K + 1)
#
# for val in A:
#     C[val] += 1
#
# B = []
# for i in range(K+1):
#     B += [i] * C[i]
#
# print(B)

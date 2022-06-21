import sys
sys.stdin = open('4869.txt')
N = 4 # 길이
def paper(n): # 현재 종이의 길이
    if n > N : # n < 0
        return 0
    if n == N: # n == 0
        return 1
    else:
        ret = paper(n + 1)
        ret += paper(n + 2)
        ret += paper(n + 2)
        return ret
result = paper(0)
print(result)





import sys
sys.stdin = open('1989.txt')

T = int(input())

for i in range(T):
    word = list(input())

    N = len(word)

    for j in range(N//2):
        if word[j] != word[N-1-j]:
            print(f'#{i + 1} 0')
            break
    else:
        print(f'#{i + 1} 1')



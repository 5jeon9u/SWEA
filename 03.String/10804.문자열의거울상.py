import sys
sys.stdin = open('10804.txt')

T = int(input())

for i in range(T):
    word = list(input())

    word_dict = {'b' : 'd', 'd' : 'b', 'p' : 'q', 'q' : 'p'}

    for j in range(len(word)):
        word[j] = word_dict.get(word[j])

    N = len(word)

    for k in range(N//2):
        word[k], word[N - 1 - k] = word[N - 1 - k], word[k]

    print(f'#{i+1}',''.join(word))
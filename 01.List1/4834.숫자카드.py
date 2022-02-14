import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int, input()))

    card_count = [0] * 10 # 각 카드의 누적 장수를 저장할 리스트(인덱스 값 = 카드 번호)

    for i in range(0, len(arr)):
        card_count[arr[i]] += 1

    max_count = 0 # 최대 카드 장수
    max_number = 0 # 최대 카드 장수를 가진 숫자

    for j in range(0, len(card_count)):
        if max_count <= card_count[j]:
            max_count = card_count[j]
            max_number = j

    print(f'#{tc + 1} {max_number} {max_count}')


N, M = map(int, input().split())

# 책이 있는 경우
if N > 0:
    books = list(map(int, input().split()))

    current_weight = 0
    boxes_count = 1

    for book in books:
        if current_weight + book <= M:  # 현재 상자에 책을 담을 수 있는 경우
            current_weight += book
        else:  # 새로운 상자가 필요한 경우
            boxes_count += 1
            current_weight = book

    print(boxes_count)
else:
    print(0)  # 책이 하나도 없는 경우
import sys
import heapq

input = sys.stdin.read

def minimize_card_sum(cards, m):
    heapq.heapify(cards)
    
    for _ in range(m):
        first = heapq.heappop(cards)
        second = heapq.heappop(cards)
        new_card = first + second
        heapq.heappush(cards, new_card)
        heapq.heappush(cards, new_card)
    
    return sum(cards)

data = input().split()
n, m = int(data[0]), int(data[1])
cards = list(map(int, data[2:]))

result = minimize_card_sum(cards, m)
print(result)
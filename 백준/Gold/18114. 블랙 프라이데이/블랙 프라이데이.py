def can_buy_items(N, C, weights):
    weights.sort()
    weight_set = set(weights)
    
    for w in weights:
        if w == C:
            return 1
    
    for i in range(N):
        for j in range(i + 1, N):
            if weights[i] + weights[j] == C:
                return 1
    
    for i in range(N):
        for j in range(i + 1, N):
            if weights[i] + weights[j] < C:
                needed = C - (weights[i] + weights[j])
                if needed in weight_set and needed != weights[i] and needed != weights[j]:
                    return 1
    
    return 0

N, C = map(int, input().split())
weights = list(map(int, input().split()))

print(can_buy_items(N, C, weights))
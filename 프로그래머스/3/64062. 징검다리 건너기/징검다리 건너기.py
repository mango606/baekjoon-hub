def solution(stones, k):
    start = 1
    end = 200000000
    
    while start <= end:
        temp = stones.copy()
        mid = (start + end) // 2
        cnt = 0
        
        for t in temp:
            if t - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
                
        if cnt >= k:
            end = mid - 1
        else:
            start = mid + 1
        
    return start
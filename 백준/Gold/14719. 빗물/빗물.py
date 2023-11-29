def cal_rain(H, W, blocks):
    rain = 0  # 빗물의 양을 저장할 변수
    
    for col in range(1, W - 1):
        left_max = max(blocks[:col])  # 현재 열의 왼쪽에서 가장 높은 블록
        right_max = max(blocks[col+1:])  # 현재 열의 오른쪽에서 가장 높은 블록
        
        if blocks[col] < min(left_max, right_max):
            rain += min(left_max, right_max) - blocks[col]
    
    return rain

H, W = map(int, input().split())
blocks = list(map(int, input().split()))

result = cal_rain(H, W, blocks)
print(result)

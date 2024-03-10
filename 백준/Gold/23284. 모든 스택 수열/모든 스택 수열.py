def function(cnt, next_val, n, num):
    if cnt == n:  # 모든 자리가 채워진 경우, 올바른 수열이므로 출력
        print(' '.join(map(str, num[:n])))
    else:
        for i in range(1, n+1):
            can = True  # 중복을 확인하기 위한 플래그
            num[cnt] = i  # 현재 자리에 수를 할당
            
            # 중복 확인
            for j in range(cnt):
                if num[j] == num[cnt]:  # 중복이 발견되면 can을 False로 설정
                    can = False
            
            # 올바른 수열인지 확인
            if can:
                if num[cnt - 1] < num[cnt] and num[cnt] < next_val:
                    # 직전 수보다 현재 수가 크고, 다음에 넣을 수보다 현재 수가 작다면 잘못된 수열
                    break  # 더 이상 진행하지 않음
                
                if next_val <= num[cnt]:
                    # 현재 들어온 수가 새로운 수라면 next_val 업데이트
                    function(cnt + 1, num[cnt] + 1, n, num)
                else:
                    # 현재 들어온 수가 이미 들어온 수를 꺼낸 것이라면 next_val 유지
                    function(cnt + 1, next_val, n, num)

n = int(input())
num = [0] * 11
function(0, 1, n, num)
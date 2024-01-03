def solution(d, budget):
    d.sort()    # 부서별 신청 금액을 오름차순으로 정렬
    answer = 0  # 지원 가능한 부서 개수

    for i in d:
        if budget - i >= 0:
            budget -= i     # 예산에서 해당 부서 금액 제외
            answer += 1     # 지원 부서 수 증가
        else:
            break

    return answer
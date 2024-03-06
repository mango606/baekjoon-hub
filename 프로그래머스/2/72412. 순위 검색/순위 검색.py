from itertools import combinations
from collections import defaultdict

def solution(info, query):
    # 정보 저장을 위한 딕셔너리
    info_dict = defaultdict(list)
    for inf in info:
        inf_split = inf.split()
        conditions = inf_split[:-1]  # 점수를 제외한 조건들
        score = int(inf_split[-1])  # 점수
        
        # 조건들의 모든 조합을 생성하여 딕셔너리에 저장
        for n in range(5):
            for comb in combinations(conditions, n):
                key = ''.join(comb)
                info_dict[key].append(score)
    
    # 이진 탐색을 위한 각 키별 정렬
    for key in info_dict.keys():
        info_dict[key].sort()
    
    answer = []
    for q in query:
        q_split = q.split(" and ")
        soul_food = q_split[-1].split()
        q_split[-1] = soul_food[0]
        score = int(soul_food[1])
        key = ''.join(q_split).replace("-", "")
        
        # 이진 탐색으로 조건을 만족하는 점수들의 개수 계산
        scores = info_dict[key]
        if scores:
            start, end = 0, len(scores)
            while start < end:
                mid = (start + end) // 2
                if scores[mid] >= score:
                    end = mid
                else:
                    start = mid + 1
            answer.append(len(scores) - start)
        else:
            answer.append(0)
            
    return answer
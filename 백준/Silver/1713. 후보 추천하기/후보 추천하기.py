n = int(input())
num_recommendations = int(input())
recommendations = list(map(int, input().split()))

# 사진틀에 들어간 후보를 저장하는 딕셔너리
photo_frame = {}

for i in recommendations:
    if i in photo_frame:
        # 이미 사진틀에 있는 경우 추천 수 증가
        photo_frame[i][0] += 1
    else:
        if len(photo_frame) < n:
            # 사진틀에 빈 공간이 있는 경우
            photo_frame[i] = [1, len(photo_frame)]
        else:
            # 사진틀이 가득 찬 경우, 가장 적은 추천 수의 후보 제거
            candidate_to_remove = min(photo_frame.items(), key=lambda x: (x[1][0], x[1][1]))[0]
            del photo_frame[candidate_to_remove]
            # 새 후보 추가
            photo_frame[i] = [1, len(photo_frame)]

print(' '.join(map(str, sorted(photo_frame.keys()))))
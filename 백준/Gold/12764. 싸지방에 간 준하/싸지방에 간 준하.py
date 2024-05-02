import sys
import heapq

input = sys.stdin.read

def solve():
    data = input().split()
    n = int(data[0])
    events = []
    index = 1

    # 이벤트 수집
    for _ in range(n):
        start = int(data[index])
        index += 1
        end = int(data[index])
        index += 1
        events.append((start, 'start'))
        events.append((end, 'end', start))  # 종료 이벤트와 연결된 시작 시간 포함

    events.sort()

    # 사용 가능한 자리와 자리 사용 횟수
    available = []
    usage_count = []
    # 각 시작 시간에 대한 자리 매핑
    seat_map = {}

    for event in events:
        time, event_type = event[:2]

        if event_type == 'start':
            if available:
                # 사용 가능한 자리 사용
                seat_index = heapq.heappop(available)
            else:
                # 새 자리 추가
                seat_index = len(usage_count)
                usage_count.append(0)
            
            usage_count[seat_index] += 1
            seat_map[time] = seat_index  # 시작 시간에 자리 인덱스 매핑
        else:
            # 사용 종료
            start_time = event[2]
            seat_index = seat_map[start_time]  # 연결된 시작 시간으로 자리 인덱스 찾기
            heapq.heappush(available, seat_index)

    print(len(usage_count))
    print(' '.join(map(str, usage_count)))

if __name__ == "__main__":
    solve()
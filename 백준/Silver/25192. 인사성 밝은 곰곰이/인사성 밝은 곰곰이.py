import sys
input = sys.stdin.read

def count_greetings(logs):
    greeted_people = set()
    total_greetings = 0

    for log in logs:
        if log == "ENTER":
            total_greetings += len(greeted_people)
            greeted_people.clear()
        else:
            greeted_people.add(log)

    total_greetings += len(greeted_people)

    return total_greetings

data = input().split()
n = int(data[0])  # 로그의 수 (하지만 실제로는 사용하지 않음)
logs = data[1:]   # 로그 내용
result = count_greetings(logs)
print(result)
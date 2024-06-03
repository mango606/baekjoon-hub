import sys
input = sys.stdin.read

def find_common_cds():
    data = input().strip().split('\n')
    index = 0

    while index < len(data):
        n, m = map(int, data[index].split())
        if n == 0 and m == 0:
            break
        
        index += 1
        first_cds = set()

        # 첫 번째 사람의 CD 목록
        for _ in range(n):
            first_cds.add(int(data[index]))
            index += 1
        
        # 두 번째 사람의 CD 목록
        common_count = 0
        for _ in range(m):
            cd = int(data[index])
            if cd in first_cds:
                common_count += 1
            index += 1

        print(common_count)

find_common_cds()
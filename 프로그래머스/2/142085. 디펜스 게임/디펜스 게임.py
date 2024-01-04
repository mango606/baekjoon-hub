def solution(n, k, enemy):
    answer = 0      # 진행한 라운드 수
    enemys = [0] * 1000001      # 무적권 사용한 수

    if len(enemy) <= k:
        return len(enemy)

    minX = 0

    for i in range(k):
        enemys[enemy[i]] += 1
        if minX == 0 or minX > enemy[i]:
            minX = enemy[i]

    answer = k

    for i in range(k, len(enemy)):
        if minX < enemy[i]:
            enemys[enemy[i]] += 1
            enemys[minX] -= 1
            n -= minX

            if enemys[minX] == 0:
                for j in range(minX + 1, len(enemys)):
                    if enemys[j] > 0:
                        minX = j
                        break
        else:
            n -= enemy[i]

        if n < 0:
            break

        answer += 1

    return answer
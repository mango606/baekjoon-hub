from sys import setrecursionlimit
setrecursionlimit(10000)

def solution(nodeinfo):
    nodeinfo = sorted([(x, y, i+1) for i, (x, y) in enumerate(nodeinfo)], key=lambda x: x[0])
    result = [[], []]

    def REC(nodeinfo):
        if nodeinfo:
            
            highest = (0, -1, 0)

            for idx, (x, y, n) in enumerate(nodeinfo):
                if y > highest[1]:
                    highest = (idx, y, n)

            result[0].append(highest[-1])

            left, right = nodeinfo[:highest[0]], nodeinfo[highest[0]+1:]

            REC(left), REC(right)

            result[1].append(highest[-1])

    REC(nodeinfo)
    return result
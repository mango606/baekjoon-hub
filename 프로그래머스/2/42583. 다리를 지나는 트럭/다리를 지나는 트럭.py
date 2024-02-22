from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    
    truck = deque(truck_weights)
    bridge = deque([0]*bridge_length)
    bridge_weight = 0
    
    while truck:
        time += 1
        bridge_weight -= bridge[0]
        bridge.popleft()
        
        if bridge_weight + truck[0] <= weight:
            w = truck.popleft()
            bridge_weight += w
            bridge.append(w)
        else:
            bridge.append(0)
            
    return time + bridge_length
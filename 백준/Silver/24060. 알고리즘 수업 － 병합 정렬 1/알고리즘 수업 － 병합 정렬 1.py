def merge_sort(array, start, end):
    if start < end:
        middle = (start + end) // 2
        merge_sort(array, start, middle)
        merge_sort(array, middle + 1, end)
        merge(array, start, middle, end)

def merge(array, start, middle, end):
    global comparison_count, kth_element
    left_index = start
    right_index = middle + 1
    temp_array = []
    
    while left_index <= middle and right_index <= end:
        if array[left_index] <= array[right_index]:
            temp_array.append(array[left_index])
            left_index += 1
        else:
            temp_array.append(array[right_index])
            right_index += 1
    
    while left_index <= middle:
        temp_array.append(array[left_index])
        left_index += 1
    
    while right_index <= end:
        temp_array.append(array[right_index])
        right_index += 1
    
    array_index = start
    temp_index = 0
    
    while array_index <= end:
        array[array_index] = temp_array[temp_index]
        comparison_count += 1
        if comparison_count == K:
            kth_element = array[array_index]
            break
        array_index += 1
        temp_index += 1

N, K = map(int, input().split())
array = list(map(int, input().split()))
comparison_count = 0
kth_element = -1
merge_sort(array, 0, N - 1)
print(kth_element)
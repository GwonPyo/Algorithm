# def binary_search(array, aim):
#     n = len(array)

#     pl = 0; pr = n - 1; pm = (pl + pr) // 2

#     while array[pm] != aim:
#         if array[pm] < aim:
#             pl = pm + 1
#         else:
#             pr = pm - 1

#         if pl > pr:
#             return False

#         pm = (pl + pr) // 2
    
#     return pm

# array = [1, 2, 3, 5, 7, 8, 9]

# print(binary_search(array, int(input())))

def binary_search(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    
    else:
        return binary_search(array, target, mid + 1, end)

def binary_search2(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        
        elif array[mid] > target:
            end = mid - 1

        else:
            start = mid + 1
    return 0
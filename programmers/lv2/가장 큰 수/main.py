# def solution(numbers):
    
#     def quick_sort(arr):
#         if len(arr) <= 1:
#             return arr
#         pivot = arr[0]
#         left, right = [], []
#         for i in range(1, len(arr)):
#             if int(pivot+arr[i]) < int(arr[i]+pivot):
#                 left.append(arr[i])
#             else:
#                 right.append(arr[i])
#         return quick_sort(left) + [pivot] + quick_sort(right)
    
#     numbers = list(map(str, numbers))
#     arr = quick_sort(numbers)
    
#     return str(int(''.join(arr)))

from functools import cmp_to_key

def solution(numbers):
    
    def compare(a, b):
        if a + b > b + a:
            return -1   
        else:
            return 1
    
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare))
    
    return str(int(''.join(numbers)))

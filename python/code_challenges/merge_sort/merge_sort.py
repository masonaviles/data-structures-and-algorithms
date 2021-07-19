# ALGORITHM Mergesort(arr)
#     DECLARE n <-- arr.length

#     if n > 1
#       DECLARE mid <-- n/2
#       DECLARE left <-- arr[0...mid]
#       DECLARE right <-- arr[mid...n]
#       // sort the left side
#       Mergesort(left)
#       // sort the right side
#       Mergesort(right)
#       // merge the sorted left and right sides together
#       Merge(left, right, arr)

# ALGORITHM Merge(left, right, arr)
#     DECLARE i <-- 0
#     DECLARE j <-- 0
#     DECLARE k <-- 0

def merge_sort(list):
    key = len(list)

    if key > 1:
        mid = key // 2
        left = list[0:mid]
        right = list[mid:key]
        merge_sort(left)
        merge_sort(right)
        return merge(left, right, list)

def merge(left, right, list):

    i = 0
    j = 0
    x = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            list[x] = left[i]
            i = i + 1

        else:
            list[x] = right[j]
            j = j + 1

        x = x + 1

    if i == len(left):
        list[x:] = right[j:] 
        list[x:] = left[i:]
    return list
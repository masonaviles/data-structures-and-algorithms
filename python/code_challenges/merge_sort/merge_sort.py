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

def Mergesort(arr):
    n = len(arr)
    if n > 1:
        mid = n//2
        left = arr[:mid]
        right = arr[mid:]
        Mergesort(left)
        Mergesort(right)
        Merge(left, right, arr)

def Merge(left, right, arr):
    i = 0
    j = 0
    k = 0
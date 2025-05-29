def BinarySearch(arr,k):
    l,r = 0,len(arr)-1
    
    while l <= r:
        m = (l+r)//2
        if arr[m] == k:
            print("found at Index : ", m)
            return m
        elif arr[m] < k:
            l = m + 1
        elif arr[m] > k:
            r = m-1
    return -1
arr = [1,2,3,4,5,6,7,8,9]
print(BinarySearch(arr,9))
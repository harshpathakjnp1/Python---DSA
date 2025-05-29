def linearSearch(arr,k):
    for i in range(len(arr)):
        if arr[i] == k:
            print("index is : ",i)
            return i
    print("not found")
    return -1



arr = [8,5,7,2,9,3]
k = int(input("Enter Value to Search - "))
linearSearch(arr,k)

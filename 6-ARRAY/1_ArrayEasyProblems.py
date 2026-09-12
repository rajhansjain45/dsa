# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 1: Largest element of array
def LargestArrayElement(arr):
    big = arr[0]
    for i in range(len(arr)):
        if arr[i]>=big:
            big = arr[i]
    print(f'largest element : {big}')
# LargestArrayElement(arr=[1,6,4,7,9])
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 2: Second largest element of array
# WORST solution : sort the array and pick the last and second last element.
# BETTER solution :
def SecondLargestAndSmallestArrayElement(arr):
    small = min(arr)
    second_small = float('inf')
    large = max(arr)
    second_large = float('-inf')

    for i in range(len(arr)):

        if second_small>arr[i] and arr[i] != small:
            second_small = arr[i]

        if second_large<arr[i] and arr[i] != large:
            second_large = arr[i] 
        
    print("Second smallest is", second_small)
    print("Second largest is", second_large)

# SecondLargestAndSmallestArrayElement(arr=[1,9,2,8,3,7,4,6])

# Optimal solution :
def SecondSmallestArrayElement(arr):
    small = float('inf')
    secondsmall = float('inf')

    for i in range(len(arr)):
        if arr[i]<small:
            secondsmall = small
            small = arr[i]
        elif arr[i]<= secondsmall and arr[i]!=small:
            secondsmall = arr[i]
    return secondsmall

def SecondLargestArrayElement(arr):
    large = float('-inf')
    secondlarge = float('-inf')
    for i in range(len(arr)):
        if arr[i]>large:
            secondlarge = large
            large = arr[i]
        elif arr[i]>=secondlarge and arr[i]!=large:
            secondlarge = arr[i]
    return secondlarge

# print(SecondLargestArrayElement(arr=[1,0,2,9,3,8,4,7,5,6]))
# print(SecondSmallestArrayElement(arr=[1,0,2,9,3,8,4,7,5,6]))

# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 3: Check if array is sorted.
def IsSortedArray(arr):
    for i in range(1,len(arr)):
        if arr[i]>=arr[i-1]: return True
        else : return False
# print(IsSortedArray(arr=[1,2,3,4,5]))

# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 4: Number of unique elements in an array.
# Brute Force Solution :
def UniqueArrayElements(arr):
    temp = set()
    ind = 0
    for i in arr:
        if i not in temp:
            temp.add(i)
            arr[ind] = i
            ind+=1
    return ind
# print(UniqueArrayElements(arr=[1,1,2,2,3,3,4,4,4]))

# Optimal Solution :
def UniqueArrayElementsOptimal(arr):
    i = 0
    for j in range(1,len(arr)):
        if arr[j]!=arr[i]:
            i+=1
            arr[i] = arr[j]
    return i + 1
# print(UniqueArrayElementsOptimal(arr=[1,1,2,2,3,3,4,4,4]))
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 5 : Left rotate an array by one element.
def LeftRotateArrayByOne(arr):
    temp = arr[0]
    for i in range(1,len(arr)):
                   arr[i-1] = arr[i]
    arr[len(arr)-1] = temp
    return arr
# print(LeftRotateArrayByOne(arr=[1,2,3,4,5]))
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 6 : Left/Right rotate an array by d elements.
# Brute force solution 
def LeftRotateArrayByD(arr,d):
    temp = arr[0:d]
    for i in range(d,len(arr)):
        arr[i-d] = arr[i]
    arr[len(arr)-d:len(arr)] = temp
    return arr
    # return arr[d:] + arr[:d]
# print(LeftRotateArrayByD(arr=[1,2,3,4,5],d=2))

# Optimal solution : Reversal Algorithm
def reverseArray(arr,start,end):
    while start<end:
        arr[start],arr[end] = arr[end],arr[start]
        start+=1
        end-=1
def LeftRotateArrayByDOptimal(arr,d):
    reverseArray(arr,0,d-1)
    reverseArray(arr,d,len(arr)-1)
    reverseArray(arr,0,len(arr)-1)

    # or we can do it as 
    # arr[:d] = arr[:d][::-1]        # Step 1: reverse first d elements
    # arr[d:] = arr[d:][::-1]        # Step 2: reverse remaining elements
    # arr[:] = arr[::-1]             # Step 3: reverse entire array
    return arr
# print(LeftRotateArrayByDOptimal(arr=[1,2,3,4,5],d=2))

# Right Rotate an array by d elements
def RightRotateArrayByDOptimal(arr, d):
    n = len(arr)
    d = d % n   # handle cases where d > n
    
    # Step 1: Reverse last d elements
    arr[n-d:] = arr[n-d:][::-1]
    
    # Step 2: Reverse first n-d elements
    arr[:n-d] = arr[:n-d][::-1]
    
    # Step 3: Reverse entire array
    arr[:] = arr[::-1]
    
    return arr

# print(RightRotateArrayByDOptimal([1,2,3,4,5], 2))
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 7 : Move all zero elements to one side/back of the array.
# Brute Force Solution : Count the number of zeroes and then move all non zero elements to the front and fill the remaining with zeroes.
def MoveZeroesToEndBF1(arr):
    count = 0
    for i in arr:
        if i==0:
            count+=1
    ind = 0
    for i in arr:
        if i!=0:
            arr[ind] = i
            ind+=1
    arr[ind:] = [0]*count
    return arr

def MoveZeroesToEndBF2(arr):
    temp = []
    for i in arr:
        if i!=0:
            temp.append(i)
    temp += [0]*(len(arr)-len(temp))
    return temp

# Optimal Solution : Two pointer approach 
def MoveZeroesToEndOptimal(arr):
    j = -1
    for i in range(len(arr)):
        if arr[i] == 0:
            j = i
            break
    if j == -1: return arr

    for i in range(j+1,len(arr)):
        if arr[i]!=0:
            arr[i],arr[j] = arr[j],arr[i]
            j+=1
    return arr
# print(MoveZeroesToEndOptimal(arr=[0,1,0,3,12]))
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 8 : Linear search in an array.
def LinearSearchArray(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
# print(LinearSearchArray(arr=[1,2,3,4,5],target=3))
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 9 : Union/Intersection of two sorted arrays.
# Brute Force Solution : Combine both arrays and then remove duplicates using set.
def UnionOfTwoSortedArrays(arr1,arr2):
    tump = set()
    for i in arr1:
        tump.add(i)
    for i in arr2:
        tump.add(i)
    return list(tump)
# print(UnionOfTwoSortedArrays(arr1=[1,2,3,4,5],arr2=[4,5,6,7,8]))

# Optimal Solution : Two pointer approach
def UnionOfTwoSortedArraysOptimal(arr1,arr2):
    i=j=0
    union = []
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            if not union or union[-1]!=arr1[i]:
                union.append(arr1[i])
                i+=1
        elif arr1[i]>arr2[j]:
            if not union or union[-1]!=arr2[j]:
                union.append(arr2[j])
                j+=1
        else:
            if not union or union[-1]!=arr1[i]:
                union.append(arr1[i])
            i+=1
            j+=1
    while i<len(arr1):
        if not union or union[-1]!=arr1[i]:
            union.append(arr1[i])
        i+=1
    while j<len(arr2):
        if not union or union[-1]!=arr2[j]:
            union.append(arr2[j])
        j+=1
    return union
# print(UnionOfTwoSortedArraysOptimal(arr1=[1,2,3,4,5],arr2=[4,5,6,7,8]))

def IntersectionOfTwoSortedArrays(arr1,arr2):
    i=j=0
    visited = [0]*len(arr2)  
    intersection = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j] and visited[j] == 0:
                intersection.append(arr1[i])
                visited[j] = 1
                break
            if arr1[i] < arr2[j]: break
    return intersection
# print(IntersectionOfTwoSortedArrays(arr1=[1,2,3,4,5],arr2=[4,5,5,6,7,8]))

def IntersectionOfTwoSortedArraysOptimal(arr1,arr2):
    i=j=0
    intersection = []
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            i+=1
        elif arr1[i]>arr2[j]:
            j+=1
        else:
            if not intersection or intersection[-1]!=arr1[i]:
                intersection.append(arr1[i])
            i+=1
            j+=1
    return intersection
# print(IntersectionOfTwoSortedArraysOptimal(arr1=[1,2,3,4,5],arr2=[4,5,6,7,8]))
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 10 : Missing number in an array of n-1 elements.
# Brute force solution : nested loop aproach
def MissingNumberInArray(arr):
    n = len(arr)
    for i in range(1,n+1):
        found = False
        for j in range(n-1):
            if arr[j] == i:
                found = True
                break
        if not found:
            return i
# print(MissingNumberInArray(arr=[1,2,4,5]))

# Betetr solution : Using hashing
def MissingNumberInArrayHashing1(arr):
    n = len(arr) + 1 # since one number is missing, the length of the array is n-1
    visited = {i:0 for i in range(1,n+1)}
    for nums in arr: 
        if nums in visited:
            visited[nums]+=1
    for k,v in visited.items():
        if v == 0:
            return k
# print(MissingNumberInArrayHashing1(arr=[1,2,4,5]))

def MissingNumberInArrayHashing2(arr):
    n = len(arr)+1
    visited = [0]*(n+1)
    for i in range(n-1):
        visited[arr[i]]+=1
    for i in range(1,n):
        if visited[i] == 0:
            return i
    return -1
# print(MissingNumberInArrayHashing2(arr=[1,2,4,5]))

# Optimal solution : Using sum formula n(n+1)/2
def MissingNumberInArrayOptimal1(arr):
    n = len(arr)+1
    totalSum = n*(n+1)//2
    arrSum = sum(arr)
    return totalSum - arrSum
# print(MissingNumberInArrayOptimal(arr=[1,2,4,5]))

def MissingNumberInArrayOptimal2(arr):
    n = len(arr)+1
    totalXorSum = 0
    arrXorSum = 0
    for i in range(1,n+1):
        totalXorSum ^=i
    for i in range(n-1):
        arrXorSum ^=arr[i]
    return totalXorSum ^ arrXorSum 
# print(MissingNumberInArrayOptimal2(arr=[1,2,4,5]))

# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 11 : Find maximum consective 1's in a binary array.
def MaxConsecutiveOnes(arr):
    count, maxCount = 0,0
    for i in range(len(arr)):
        if arr[i] == 1:
            count+=1
        else:
            count = 0
        maxCount = max(maxCount,count)
    return maxCount
# print(MaxConsecutiveOnes(arr=[1,1,0,1,1,1,0,1,1]))

# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 12 : Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.
# Brute force solution : using nested loop  aaproach
def SingleNumber(arr):
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count+=1
        if count == 1:
            return arr[i]
# print(SingleNumber(arr=[2,2,1]))

# Better solution : using hashing
def SingleNumberHashing(arr):
    visited = {}
    for i in arr:
        visited[i] = visited.get(i,0)+1
    for k,v in visited.items():
        if v == 1:
            return k
# print(SingleNumberHashing(arr=[2,2,1]))

# Optimal solution : using XOR operator
def SingleNumberOptimal(arr):
    xorSum = 0
    for i in arr:
        xorSum ^=i
    return xorSum
# print(SingleNumberOptimal(arr=[2,2,1]))

# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 13 : Longest Subarray with given Sum K(Positives)
# Brute force solution : using nested loop approach
def LongestSubarrayWithSumK(arr,k):
    maxlen = 0
    for i in range(len(arr)):
        # sum = 0
        for j in range(i,len(arr)):
            # sum = sum + arr[j]
            if sum(arr[i:j+1]) == k:
                maxlen = max(maxlen,j-i+1)
            # sum = 0
            # for m in range(i,j+1):
            #     sum+=arr[m]
            # if sum == k:
            #     maxlen = max(maxlen,j-i+1)
    return maxlen
# print(LongestSubarrayWithSumK(arr=[1,2,3,4,5],k=9))

# Optimal solution : using sliding window approach
def LongestSubarrayWithSumKOptimal(arr,k):
    n = len(arr)
    left = 0
    right = 0
    currentSum = 0
    maxlen = 0
    while right<n:
        currentSum+=arr[right]
        while currentSum>k:
            currentSum-=arr[left]
            left+=1
        if currentSum == k:
            maxlen = max(maxlen,right-left+1)
        right+=1
    return maxlen
# print(LongestSubarrayWithSumKOptimal(arr=[1,2,3,4,5],k=9))
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 14 : Longest Subarray with given Sum K(Positives &Negatives)
def LongestSubarrayWithSumKOptimal(arr,k):
    visited = {0:-1} # to handle the case when the subarray with sum k starts from index 0
    currentSum = 0
    maxLen = 0

    for i in range(len(arr)):
        currentSum+=arr[i]
        if currentSum-k in visited:
            maxLen = max(maxLen,i-visited[currentSum-k])
        if currentSum not in visited:
            visited[currentSum] = i
    return maxLen
# print(LongestSubarrayWithSumKOptimal(arr=[1,-1,5,-2,3],k=3))
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
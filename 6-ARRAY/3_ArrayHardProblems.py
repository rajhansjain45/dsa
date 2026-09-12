# PROBLEM 1 : Pascles Triangle
# Variety 1 : Generate first n rows of pascal triangle
def GenerateNthRowPascalTriangle(n):
    row = []
    val = 1
    row.append(val)
    for i in range(1,n):
        val = val*(n-i)//i
        row.append(val)
    return row

def GeneratePascalTriangle(n):
    triangle = []
    for i in range(1,n+1):
        triangle.append(GenerateNthRowPascalTriangle(i))
    return triangle
# print(GeneratePascalTriangle(5))

# Variety 2 : Generate nth row of pascal triangle
def GenerateNthRowPascalTriangle(n):
    row = []
    val = 1
    row.append(val)
    for i in range(1,n):
        val = val*(n-i)//i
        row.append(val)
    return row
# print(GenerateNthRowPascalTriangle(5))

# Variety 3 : Generate kth element of nth row of pascal triangle
def GeneratePascalElement(n,k):
    element = 1
    for i in range(k):
        element = element * (n - i) // (i+1)
    return element
    
    # converting 0 based indexing to one based indexing  
    # a = n-1 
    # b = k-1
    # if a == 0 or a == b:
    #     return 1
    # else:
    #     return GeneratePascalElement(a-1,b-1) + GeneratePascalElement(a-1,b)
# print(GeneratePascalElement(5,2))

# ----------------------------------------------------------------------------
# PROBLEM 2 : Majority Element (n/3)
# brute force aproach : nested loops
def MajorityElement(arr):
    n = len(arr)
    ls = []
    for i in range(n):
        if len(ls) == 0 or arr[i] not in ls:
            count = 0
            for j in range(n):
                if arr[j] == arr[i]:
                    count += 1
            if count > n//3:
                ls.append(arr[i])
        if len(ls) == n//3:
            break
    return ls
# print(MajorityElement([1,1,1,3,3,2,2,2]))

# Better approach : using hash map
def MajorityElementHashMap(arr):
    n = len(arr)
    hashmap = {}
    list = []
    min = n//3 +1
    for i in range(n):
        # hashmap[arr[i]] += 1 if arr[i] in hashmap else 1 or get() function
        hashmap[arr[i]] = hashmap[arr[i]] + 1 if arr[i] in hashmap else 1
    
    for key,value in hashmap.items():
            if value == min:
                list.append(key)
    return list   
# print(MajorityElementHashMap([1,1,1,3,3,2,2,2]))

# Optimal approach : Boyer-Moore Voting Algorithm
def MajorityElementBoyerMoore(arr):
    n = len(arr)
    count1 = 0
    count2 = 0
    candidate1 = None
    candidate2 = None
    # step 1 : find the candidates
    for i in range(n):
        if count1 == 0 and candidate2 != arr[i]:
            count1 = 1
            candidate1 = arr[i]
        elif count2 == 0 and candidate1 != arr[i]:
            count2 = 1
            candidate2 = arr[i]
        elif arr[i] == candidate1:
            count1 += 1
        elif arr[i] == candidate2:
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1
        
    # step 2 : verify the candidates
    count1 = 0
    count2 = 0
    for i in range(n):
        if arr[i] == candidate1:
            count1 += 1
        elif arr[i] == candidate2:
            count2 += 1
    
    # for i in arr:
    #     if i == candidate1:
    #         count1 += 1
    #     elif i == candidate2:
    #         count2 += 1
    
    result = []
    minimum = n//3 + 1
    if count1 >= minimum:
        result.append(candidate1)
    if count2 >= minimum and candidate2 != candidate1:
        result.append(candidate2)
    return result

# print(MajorityElementBoyerMoore([1,1,1,3,3,2,2,2]))

# ----------------------------------------------------------------------------
# PROBLEM 3 : 3Sum - Given an array of integers, find all unique triplets ([arr[a], arr[b], arr[c]] such that i!=j, j!=k, k!=i) in the array which gives the sum of zero.
# Brute force : nested loops
def ThreeSum(arr):
    Set  = set()
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if arr[i] + arr[j] + arr[k] == 0:
                    # for unique triplets 
                    triplet = tuple(sorted([arr[i], arr[j], arr[k]]))
                    Set.add(triplet)
    return [list(triplet) for triplet in Set]
# print(ThreeSum([-1,0,1,2,-1,-4]))

# Better approach : using Hashing 
def ThreeSumHashing(arr):
    Set = set()
    n = len(arr)
    for i in range(n):
        hashSet = set()
        for j in range(i+1,n):
            compliment = -(arr[i]+arr[j])
            if compliment in hashSet:
                triplet = tuple(sorted([arr[i], arr[j], compliment]))
                Set.add(triplet)
            hashSet.add(arr[j])
    return [list(triplet) for triplet in Set]
# print(ThreeSumHashing([-1,0,1,2,-1,-4]))

# Optimal approach : using sorting and two pointers
def ThreeSumTwoPointers(arr):
    arr.sort()
    n = len(arr)
    ans = []
    for i in range(n):
        if i>0 and arr[i] == arr[i-1]:
            continue
        left = i+1
        right = n-1
        while left <right:
            sum = arr[i] +arr[left] + arr[right]
            if sum == 0:
                ans.append([arr[i],arr[left],arr[right]])
                left += 1
                right -= 1
                
                while left < right and arr[left] == arr[left-1]:
                    left += 1
                while left < right and arr[right] == arr[right+1]:
                    right -= 1
                
            elif sum < 0:
                left += 1
            else:
                right -= 1
    return ans
# print(ThreeSumTwoPointers([-1,0,1,2,-1,-4]))

# ------------------------------------------------------------------------------
# PROBLEM 4 : 4Sum - Given an array of integers, find all unique quadruplets ([arr[a], arr[b], arr[c], arr[d]] such that i!=j, j!=k, k!=l, l!=i) in the array which gives the sum of target.
# Brute force : nested loops
def FourSum(arr,target):
    Set = set()
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    if arr[i] + arr[j] + arr[k] + arr[l] == target:
                        quadruplet = tuple(sorted([arr[i], arr[j], arr[k], arr[l]]))
                        Set.add(quadruplet)
    return [list(quadruplet) for quadruplet in Set]
# print(FourSum([1,0,-1,0,-2,2],1))

# Better approach : using Hashing
def FourSumHashing(arr,target):
    n = len(arr)
    Set = set()
    for i in range(n):
        for j in range(i+1,n):
            hashset = set()
            for k in range(j+1,n):
                compliment = target - (arr[i] + arr[j] + arr[k])
                if compliment in hashset:
                    quadruplet = tuple(sorted([arr[i], arr[j], arr[k], compliment]))
                    Set.add(quadruplet)
                # we can also add arr[k] to hashset after checking for compliment because we need to ensure that k is not equal to i and j
                hashset.add(arr[k])
    return [list(quadruplet) for quadruplet in Set]
# print(FourSumHashing([1,0,-1,0,-2,2],1))

# Optimal approach : using sorting and two pointers
def FourSumTwoPointers(arr,target):
    n = len(arr)
    arr.sort()
    ans = []
    for i in range(n):
        if i>0 and arr[i] == arr[i-1]:
            continue
        for j in range(i+1,n):
            if j>i+1 and arr[j] == arr[j-1]:
                continue
            left = j+1
            right = n-1
            while left < right:
                sum = arr[i] + arr[j] + arr[left] + arr[right]
                if sum == target:
                    ans.append([arr[i],arr[j],arr[left],arr[right]])
                    left += 1
                    right -= 1

                    while left < right and arr[left] == arr[left-1]:
                        left += 1
                    while left < right and arr[right] == arr[right+1]:
                        right -= 1
                
                elif sum < target:
                    left += 1
                else :
                    right -= 1
    return ans
# print(FourSumTwoPointers([1,0,-1,0,-2,2],1))
# -------------------------------------------------------------------------------

# PROBLEM 5 : Longest subarray with sum zero
# Brute force : nested loop
def LongestSubarrayWithSumZero(arr):
    n = len(arr)
    maxi = 0
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += arr[j]
            if sum == 0:
                maxi = max(maxi, j-i+1)
    return maxi
# print(LongestSubarrayWithSumZero([1,-1,0,2,-2])) 

# Optimal aproach : using Hashing
def LongestSubarrayWithSumZeroHashing(arr):
    n = len(arr)
    hashmap = {0:-1} # to handle the case when the sum is zero from the beginning of the array
    sum = 0
    maxi = 0
    for i in range(n):
        sum += arr[i]
        if sum in hashmap:
            maxi = max(maxi, i - hashmap[sum])
        else:
            hashmap[sum] = i
    return maxi
# print(LongestSubarrayWithSumZeroHashing([1,-1,0,2,-2]))
# --------------------------------------------------------------------------------
# PROBLEM 6 : Number of subarrays with XOR k
# Brute force : nested loop
def SubarraysWithXORK(arr,t):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i,n):
            xor = 0
            for k in range(i,j+1):
                xor ^= arr[k]
            if xor == t:
                count += 1
    return count
# print(SubarraysWithXORK([4,2,2,6,4],6))

# Better aproach : nested loops
def SubarraysWithXORK(arr,t):
    n = len(arr)
    count = 0
    for i in range(n):
        xor = 0
        for j in range(i,n):
            xor ^= arr[j]
            if xor == t:
                count += 1
    return count
# print(SubarraysWithXORK([4,2,2,6,4],6))

# Optimal approach : using Hashing
def SubarraysWithXORKHashing(arr,t):
    n = len(arr)
    count = 0
    hashmap = {0:1} # to handle the case when the xor is zero from the beginning of the array
    xor = 0
    for i in range(n):
        xor ^= arr[i]
        compliment = xor^t
        if compliment in hashmap:
            count += hashmap[compliment]
        hashmap[xor] = hashmap.get(xor, 0) + 1
    return count
# print(SubarraysWithXORKHashing([4,2,2,6,4],6))

# --------------------------------------------------------------------------------
# PROBLEM 7 : Merge overlapping sub intervals
# Brute firce : nested loops
def MergeIntervals(ArrIntervals):
     n = len(ArrIntervals)
     ArrIntervals.sort()
     MergedIntervals = []
     for i in range(n):
         start = ArrIntervals[i][0]
         end = ArrIntervals[i][1]
         if MergedIntervals and MergedIntervals[-1][1] >= end: # to handle the case when the current interval is completely overlapped by the previous interval
                continue
         for j in range(i+1,n):
             if ArrIntervals[j][0] <= end:
                 end = max(end, ArrIntervals[j][1])
             else:
                 break
         MergedIntervals.append([start,end])
     return MergedIntervals
# print(MergeIntervals([[1,3],[2,6],[8,10],[15,18]]))

# Optimal aproach : using sorting and merging
def MergeIntervalsOptimal(ArrIntervals):
    ArrIntervals.sort()
    MergedIntervals = []
    for interval in ArrIntervals:
        if not MergedIntervals or MergedIntervals[-1][1] < interval[0]:
            MergedIntervals.append(interval)
        else:
            MergedIntervals[-1][1] = max(MergedIntervals[-1][1], interval[1])
    return MergedIntervals
# print(MergeIntervalsOptimal([[1,3],[2,6],[8,10],[15,18]]))

# --------------------------------------------------------------------------------
# PROBLEM 8 : Merge sorted arrays without extra spaces
# Brute force : using extra space
def MergeSortedArrays(arr1,arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    merged = []
    left = 0
    right = 0
    index = 0
    while left < n1 and right < n2:
        if arr1[left] < arr2[right]:
            merged.append(arr1[left])
            left += 1
            index += 1
        else:
            merged.append(arr2[right])
            right += 1
            index += 1
    
    while left < n1:
        merged.append(arr1[left])
        left += 1
        index += 1
    
    while right < n2:
        merged.append(arr2[right])
        right += 1
        index += 1

    for i in range(n1+n2):
        if i < n1:
            arr1[i] = merged[i]
        else:
            arr2[i-n1] = merged[i]
    return arr1,arr2
# print(MergeSortedArrays([1,3,5],[2,4,6]))

# Optimal approach 1 : swapping and sorting
def MergeSortedArraysOptimal1(arr1,arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    left = n1-1
    right = 0
    while left >= 0 and right < n2:
        if arr1[left] > arr2[right]:
            arr1[left],arr2[right] = arr2[right],arr1[left]
            left -= 1
            right += 1 
        else:
            break
    arr1.sort()
    arr2.sort()
    return arr1,arr2
# print(MergeSortedArraysOptimal1([1,3,5],[2,4,6]))

# Optimal approach 2 : using gap method
def MergeSortedArraysOptimal2(arr1,arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    gap = (n1+n2+1)//2
    while gap > 0:
        left = 0
        right = left + gap
        while right < n1+n2:
            # when and left and right both are in arr1
            if left < n1 and right < n1:
                if arr1[left] > arr1[right]:
                    arr1[left],arr1[right] = arr1[right],arr1[left] 
            # when left is in arr1 and right is in arr2
            elif left < n1 and right >= n1:
                if arr1[left] > arr2[right-n1]:
                    arr1[left],arr2[right-n1] = arr2[right-n1],arr1[left]
            # when and left and right both are in arr2
            else:
                # if arr2[left-n1] > arr2[right-n1]:
                    arr2[left-n1],arr2[right-n1] = arr2[right-n1],arr2[left-n1]
            left += 1
            right += 1
        if gap == 1:
            break
        gap = (gap+1)//2
    return arr1,arr2
# print(MergeSortedArraysOptimal2([1,3,5],[2,4,6]))

# --------------------------------------------------------------------------------
# PROBLEM 9 : counting inversions in an array - An inversion is a pair of indices (i, j) such that i < j and arr[i] > arr[j].
# Brute force : nested loops
def CountInversions(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                count += 1
    return count
# print(CountInversions([1,20,6,4,5]))

# Optimal approach : using merge sort - we can count the inversions while merging the two halves of the array
def Merge(arr, low, mid, high):
    temp = []
    left, right = low , mid+1
    count = 0
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            count += (mid - left + 1) # all the elements from left to mid will be greater than arr[right]
            right += 1
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1
    for i in range(low, high+1):
        arr[i] = temp[i-low]
    return count

def MergeSort(arr, low, high):
    count = 0
    if low >= high:
        return count
    mid = (low + high) // 2
    count += MergeSort(arr, low, mid)
    count += MergeSort(arr, mid+1, high)
    count += Merge(arr, low, mid, high)
    return count

def CountInversionsOptimal(arr):
    return MergeSort(arr, 0, len(arr)-1)
# print(CountInversionsOptimal([1,20,6,4,5]))

# --------------------------------------------------------------------------------
# PROBLEM 10 : Count reverse pairs in an array - A reverse pair is a pair of indices (i, j) such that i < j and arr[i] > 2*arr[j].
# Brute force : nested loops
def CountReversePairs(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] > 2*arr[j]:
                count += 1
    return count
# print(CountReversePairs([1,3,2,3,1]))

# Optimal approach : using merge sort - we can count the reverse pairs while merging the two halves of the array

def CountReversePairs(arr,low,mid,high):
    count = 0
    right = mid + 1
    for left in range(low, mid+1):
        while right <= high and arr[left] > 2*arr[right]:
            right += 1
        count += (right - (mid + 1)) # all the elements from mid+1 to right-1 will be less than arr[left]/2
    return count

def MergeSort(arr, low, high):
    count = 0
    if low >= high:
        return count
    mid = (low + high) // 2
    count += MergeSort(arr, low, mid)
    count += MergeSort(arr, mid+1, high)
    count += CountReversePairs(arr, low, mid, high)
    # we need to merge the two halves of the array after counting the reverse pairs
    Merge(arr, low, mid, high)
    return count
def CountReversePairsOptimal(arr):
    return MergeSort(arr, 0, len(arr)-1)
# print(CountReversePairsOptimal([1,3,2,3,1]))

# --------------------------------------------------------------------------------
# PROBLEM 11 : Find missing and repeating number in an array - Given an array of n integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number and one missing number. Find these two numbers.
# Brute force : using nested loops
def FindMissingAndRepeating(arr):
    n = len(arr)
    missing = -1
    repeating = -1
    for i in range(1,n+1):
        count = 0
        for j in range(n):
            if arr[j] == i:
                count += 1
        if count == 0:
            missing = i
        elif count == 2:
            repeating = i   
    return [missing, repeating]
# print(FindMissingAndRepeating([3,1,2,5,3]))

# Better approach : using hashing
def FindMissingAndRepeatingHashing(arr):
    n = len(arr)
    hashmap = {}
    for num in arr:
        hashmap[num] = hashmap.get(num, 0) + 1
    missing = -1
    repeating = -1
    for i in range(1,n+1):
        if i not in hashmap:
            missing = i
        elif hashmap[i] == 2:
            repeating = i
    return [missing, repeating]
# print(FindMissingAndRepeatingHashing([3,1,2,5,3]))

# Optimal approach : using mathematical equations - we can use the formula for the sum of first n natural numbers 
# and the sum of squares of first n natural numbers to find the missing and repeating numbers
def FindMissingAndRepeatingOptimal(arr):
    n = len(arr)
    SumN = n*(n+1)//2
    SumSquaresN = n*(n+1)*(2*n+1)//6
    SumArr = 0
    SumSquaresArr = 0
    for num in arr:
        SumArr += num
        SumSquaresArr += num*num
    
    # let x be the missing number and y be the repeating number
    # we have two equations:
    # 1. x - y = SumN - SumArr
    # 2. x^2 - y^2 = SumSquaresN - SumSquaresArr
    # we can solve these two equations to find x and y
    x_minus_y = SumN - SumArr
    x_plus_y = (SumSquaresN - SumSquaresArr) // x_minus_y
    x = (x_minus_y + x_plus_y) // 2
    y = x_plus_y - x
    return [x, y]
# print(FindMissingAndRepeatingOptimal([3,1,2,5,3]))
# PROBLEM 1 : Two sum problrm
# Brute force : nested loops
def TwoSum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == target:
                return [i,j]
    return None
# print(TwoSum([2,7,11,15], 9))

# Better solution : using Hashmap
def TwoSumHash(arr, target):
    hashmap = {}
    for i,j in enumerate(arr):
        if target - j in hashmap:
            return [hashmap[target-j],i]
        hashmap[j] = i
    return None
# print(TwoSumHash([2,7,11,15], 9))

# Optimal solution : using two pointers
def TwoSumTwoPointers(arr, target):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] +arr[right] == target:
            return[left,right]
        
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1
    return None
# print(TwoSumTwoPointers([2,7,11,15], 9))

# ----------------------------------------------------------------------
# PROBLEM 2 : Sort an array of 0s, 1s and 2s
# Brute force : any sorting algorithm

# Better solution : counting sort
def Sort012(arr):
    a,b,c = 0,0,0
    for i in arr:
        if i == 0: a+=1
        elif i == 1: b+=1
        else: c+=1
    for i in range(a):arr[i] = 0
    for i in range(a,a+b):arr[i] = 1
    for i in range(a+b,a+b+c):arr[i] = 2
    return arr
    # count = [0,0,0]
    # for i in arr:
    #     count[i] += 1
    # index = 0
    # for i in range(3):
    #     for j in range(count[i]):
    #         arr[index] = i
    #         index += 1
    # return arr
# print(Sort012([0,1,2,0,1,2]))

# Optimal solution : Dutch National Flag Algorithm
def Sort012DNF(arr):
    low , mid , high = 0, 0, len(arr)-1
    while mid<=high:
        if arr[mid] == 0:
            arr[low],arr[mid] = arr[mid],arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid],arr[high] = arr[high],arr[mid]
            high -= 1
    return arr
# print(Sort012DNF([0,1,2,0,1,2]))

# ----------------------------------------------------------------------
# PROBLEM 3 : Majority Element (element that appears more than n/2 times)
# Brute force : nested loops
def MajorityElement(arr):
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
        if count > len(arr)//2:
            return arr[i]
    return None
# print(MajorityElement([2,2,1,1,1,2,2]))

# Better solution : using Hashmap
def MajorityElementHash(arr):
    hashmap = {}
    for i in arr:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1
    for key in hashmap:
        if hashmap[key] > len(arr)//2:
            return key
    return None
# print(MajorityElementHash([2,2,1,1,1,2,2]))

# Optimal solution : Boyer-Moore Voting Algorithm
def MajorityElementBoyerMoore(arr):
    count = 0
    candidate = None
    for num in arr:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    c = 0
    for num in arr:
        if num == candidate:
            c += 1
    return candidate if c > len(arr)//2 else None
# print(MajorityElementBoyerMoore([2,2,1,1,1,2,2]))

# ----------------------------------------------------------------------
# PROBLEM 4 : Maximum subarray sum
# Brute force : 3 nested loops
# Better solution : 2 nested loops
def MaxSubarraySum(arr):
    maxSum = float('-inf')
    for i in range(len(arr)):
        currentSum = 0
        for j in range(i,len(arr)):
            currentSum += arr[j]
            maxSum = max(maxSum, currentSum)
    return maxSum
# print(MaxSubarraySum([-2,1,-3,4,-1,2,1,-5,4]))

# Optimal solution : Kadane's Algorithm
def MaxSubarraySumKadane(arr):
    maxSum = float('-inf')
    currentSum = 0
    for i in range(len(arr)):
        currentSum += arr[i]
        
        if currentSum > maxSum:
            maxSum = currentSum
        
        if currentSum < 0:
            currentSum = 0

        # currentSum = max(arr[i], currentSum + arr[i])
        # maxSum = max(maxSum, currentSum)
    return maxSum
# print(MaxSubarraySumKadane([-2,1,-3,4,-1,2,1,-5,4]))

def SubarrayWithMaxSubarraySumKadane(arr):
    maxSum = float('-inf')
    currentSum = 0
    ansStart , ansEnd , tempStart = 0,0,0
    for i in range(len(arr)):
        currentSum += arr[i]
        
        if currentSum > maxSum:
            maxSum = currentSum
            ansStart = tempStart
            ansEnd = i

        if currentSum < 0:
            currentSum = 0
            tempStart = i + 1
        
    # Printing the subarray
    print("The subarray is: [", end="")
    for i in range(ansStart, ansEnd + 1):
        print(arr[i], end=" ")
    print("]")

    return maxSum

# print(SubarrayWithMaxSubarraySumKadane([-2,1,-3,4,-1,2,1,-5,4]))

# ----------------------------------------------------------------------
# PROBLEM 5 : Stock Buy and Sell - find the maximum profit that can be achieved by buying and selling a stock on different days
def StockBuySell(arr):
    minPrice = float('inf')
    maxProfit = 0
    for price in arr:
        # If current price is less than min_price, update min_price
        if price < minPrice:
            minPrice = price
        # Else calculate profit and update max_profit if it's greater
        else :
            maxProfit = max(maxProfit, price - minPrice)
    return maxProfit
# print(StockBuySell([7,1,5,3,6,4]))
# ----------------------------------------------------------------------
# PROBLEM 6 : Rearrange Array Elements by Sign
# Variety 1 : Positive and negative numbers are equal in count
# Brute force : using extra space
def RearrangeBySign(arr):
    pos , neg = [], []
    for i in arr:
        if i >= 0:
            pos.append(i)
        else:
            neg.append(i)
    for i in range(len(arr)//2):
        arr[2*i] = pos[i]
        arr[2*i + 1] = neg[i]
    return arr
# print(RearrangeBySign([3,1,-2,-5,2,-4]))

# Optimal solution : using two pointers
def RearrangeBySignTwoPointers(arr):
    n = len(arr)
    i,j = 0,1
    ansArr = []
    for k in range(n):
        if arr[k] >= 0:
            ansArr.append(arr[i])
            i += 2
        else:
            ansArr.append(arr[j])
            j += 2
    return ansArr
# print(RearrangeBySignTwoPointers([3,1,-2,-5,2,-4]))

# Variety 2 : Positive and negative numbers are not equal in count
def RearrangeBySignUnequal(arr):
    pos , neg = [] , []
    for i in arr:
        if i >= 0:
            pos.append(i)
        else: 
            neg.append(i)
    
    if len(pos) > len(neg):
        for i in range(len(neg)):
            arr[2*i] = pos[i]
            arr[2*i + 1] = neg[i]
        index = 2*len(neg)
        for i in range(len(neg), len(pos)):
                arr[index] = pos[i]
                index += 1

    if len(neg) >= len(pos):
        for i in range(len(pos)):
            arr[2*i] = pos[i]
            arr[2*i + 1] = neg[i]
        index = 2*len(pos)
        for i in range(len(pos), len(neg)):
                arr[index] = neg[i]
                index += 1
    return arr
# print(RearrangeBySignUnequal([3,1,-2,-5,2,-4,-6]))

# -----------------------------------------------------------------------
# PROBLEM 7 : Next Permutation - rearrange numbers to get the next greater permutation
# Optimal solution : using three steps
def NextPermutation(arr):
    n = len(arr)
    index = -1
    # Step 1 : find the rightmost pair of indices (i,j) such that arr[i] < arr[j]
    for i in range(n-2,-1,-1):
        if arr[i]<arr[i+1]:
            index = i
            break
    # If no such pair exists, the permutation is the last permutation    
    if index == -1:
         arr.reverse()
    
    # Step 2 : find the rightmost index j such that arr[index] < arr[j]
    for i in range(n-1, index,-1):
        if arr[index] < arr[i]:
            # Step 3 : swap arr[index] and arr[j]
            arr[index],arr[i] = arr[i],arr[index]
            break

    # Step 4 : reverse the subarray from index + 1 to the end of the array
    arr[index+1:] = reversed(arr[index+1:])
    return arr
# print(NextPermutation([1,2,3]))
# -----------------------------------------------------------------------
# PROBLEM 8 : Leaders in an Array - an element is a leader if it is greater than all the elements to its right
# Brute force : nested loops
def LeadersInArray(arr):
    leaders = []
    for i in range(len(arr)):
        isLeader = True
        for j in range(i+1, len(arr)):
            if arr[i] <= arr[j]:
                isLeader = False
                break
        if isLeader:
            leaders.append(arr[i])
    return leaders
# print(LeadersInArray([16,17,4,3,5,2]))

# Optimal solution : traversing from right
def LeadersInArrayOptimal(arr):
    leaders = []
    maxFromRight = float('-inf')
    for i in range(len(arr)-1, -1, -1):
        if arr[i] > maxFromRight:
            leaders.append(arr[i])
            maxFromRight = max(maxFromRight, arr[i])
    return leaders[::-1]
# print(LeadersInArrayOptimal([16,17,4,3,5,2]))

# -----------------------------------------------------------------------
# PROBLEM 9 : Longest Consecutive Sequence in an Array
# Brute force : nested loops and Linear search
def LinerSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True
    return False

def LongestConsecutiveSequence(arr):
    longest = 0
    for i in range(len(arr)):
        currentNum = arr[i]
        currentStreak = 1

        while LinerSearch(arr, currentNum + 1):
            currentNum += 1
            currentStreak +=1
            longest = max(longest, currentStreak)
    return longest
# print(LongestConsecutiveSequence([100,4,200,1,3,2]))

# Better solution : Using Sorting
def LongestConsecutiveSequenceSorting(arr):
    arr.sort()
    n = len(arr)
    longest = 1
    currentStreak = 0
    lastSmaller = float('-inf')
    for i in range(n):
        if arr[i] - 1 == lastSmaller:
            currentStreak += 1
            lastSmaller = arr[i]
        elif arr[i] != lastSmaller:
            longest = max(longest, currentStreak)
            currentStreak = 1
            lastSmaller = arr[i]
    longest = max(longest, currentStreak)
    return longest
# print(LongestConsecutiveSequenceSorting([100,4,200,1,3,2]))

# Optimal solution : Using HashSet
def LongestConsecutiveSequenceHashSet(arr):
    numSet = set(arr)
    longest = 0
    for num in arr:
        if num - 1 not in numSet:
            currentNum = num
            currentStreak = 1
            while currentNum + 1 in numSet:
                currentNum += 1
                currentStreak += 1
            longest = max(longest, currentStreak)
    return longest
# print(LongestConsecutiveSequenceHashSet([100,4,200,1,3,2]))

# -----------------------------------------------------------------------
# PROBLEM 10 : Set Matrix Zeroes - if an element is 0, set its entire row and column to 0
# Brute force : using extra space to store the indices of rows and columns to be marked as zero 
def SetMatrixZeroes(matrix):
    n = len(matrix)
    m = len(matrix[0])

    def MarkRowZeros(i):
        for j in range(m):
            if matrix[i][j] != 0:
                matrix[i][j] = -1
    def MarkColZeros(j):
        for i in range(n):
            if matrix[i][j] != 0:
                matrix[i][j] = -1
    # Mark the rows and columns to be set to zero with -1
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                MarkRowZeros(i)
                MarkColZeros(j)
    # Replace all -1 with 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
    return matrix
# print(SetMatrixZeroes([[1,1,1],[1,0,1],[ 1,1,1]]))

# Better solution : using two sets to store the indices of rows and columns to be marked as zero
def SetMatrixZeroesBetter(matrix):
    n = len(matrix)
    m = len(matrix[0])
    SetRow = [0]*m
    SetCol = [0]*n

    # Mark the rows and columns to be set to zero
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                SetRow[i] = 1
                SetCol[j] = 1
    # Set the marked rows and columns to zero
    for i in range(n):
        for j in range(m):
            if SetRow[i] == 1 or SetCol[j] == 1:
                matrix[i][j] = 0
    return matrix
# print(SetMatrixZeroesBetter([[1,1,1],[1,0,1],[ 1,1,1]]))

# Optimal solution : using first row and first column as markers
def  SetMatrixZeroesOptimal(matrix):
    n = len(matrix) # Number of rows
    m = len(matrix[0]) # Number of columns
    col00 = 1 # To check if the first column needs to be set to zero
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0 # Mark the first element of the row
                if j !=0:
                    matrix[0][j] = 0 # Mark the first element of the column
                else:
                    col00 = 0 # Mark that the first column needs to be set to zero
    
    # Set the marked rows and columns to zero
    for i in range(1,n):
        for j in range(1,m):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    
    # Set the first row to zero if needed
    if matrix[0][0] == 0:
        for j in range(m):
            matrix[0][j] = 0

    # Set the first column to zero if needed
    if col00 == 0:
        for i in range(n):
            matrix[i][0] = 0
    return matrix
# print(SetMatrixZeroesOptimal([[1,1,1],[1,0,1],[ 1,1,1]]))

# -------------------------------------------------------------------------
# PROBLEM 11 : Rotate image - rotate a 2D matrix by 90 degrees clockwise
# Brute force : using extra space
def RotateImage(matrix):
    n = len(matrix)
    m = len(matrix[0])
    rotated = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            rotated[j][n-1-i] = matrix[i][j]
    return rotated
# print(RotateImage([[1,2,3],[4,5,6],[7,8,9]]))

# Optimal solution : Transpose and Reverse
def RotateImageOptimal(matrix):

    n = len(matrix)
    m = len(matrix[0])
    # Transpose
    for i in range(n):
        for j in range(i+1,m):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
    
    return matrix
# print(RotateImageOptimal([[1,2,3],[4,5,6],[7,8,9],[7,8,9]]))

# -----------------------------------------------------------------------
# PROBLEM 12 : Spiral Matrix - print the elements of a 2D matrix in spiral order
#              right -> down -> left -> up
def SpiralMatrix(matrix):
    n =len(matrix)
    m = len(matrix[0])
    left = 0 
    right = m-1
    top = 0 
    bottom = n-1
    spiral = []
    while left <= right and top <= bottom:
        # Traverse from left to right
        for j in range(left, right+1):
            spiral.append(matrix[top][j])
        top +=1 # Move top boundary down

        # Traverse from top to bottom
        for i in range(top, bottom+1):
            spiral.append(matrix[i][right])
        right -= 1 # Move right boundary left

        if top <= bottom:
            # Traverse from right to left
            for j in range(right, left-1, -1):
                spiral.append(matrix[bottom][j])
            bottom -= 1 # Move bottom boundary up
        if left <= right:
            # Traverse from bottom to top
            for i in range(bottom, top-1, -1):
                spiral.append(matrix[i][left])
            left += 1 # Move left boundary right
    return spiral
# print(SpiralMatrix([[1,2,3],[4,5,6],[7,8,9]]))

# -----------------------------------------------------------------------
# PROBLEM 13 : Number of Subarrays with Sum K
# Brute force : nested loops
def NumberSubarraysWithSumK(arr, k):
    countt = 0
    for i in range(len(arr)):
        currentSum = 0
        for j in range(i, len(arr)):
            currentSum += arr[j]
            if currentSum == k:
                countt += 1
    return countt
# print(NumberSubarraysWithSumK([1,1,1], 2))

# Optimal solution : using Hashmap and prefix sum
def NumberSubarraysWithSumKOptimal(arr, k):
    count = 0
    prefixSum = 0
    hashmap = {0:1} # To handle the case when prefixSum itself is equal to k
    for num in arr:
        prefixSum += num
        if prefixSum-k in hashmap:
            count += hashmap[prefixSum-k]
        else:
            # hashmap[prefixSum] = hashmap.get(prefixSum, 0) + 1
            # Store the current sum in the dictionary
            if prefixSum in hashmap:
                hashmap[prefixSum] += 1
            else:
                hashmap[prefixSum] = 1
    return count
# print(NumberSubarraysWithSumKOptimal([1,1,1], 2))

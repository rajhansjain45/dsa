# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 1 : Longest Substring Without Repeating Characters
# Brute force :
def LongestSubstringWithoutRepeatingCharacters(s):
    maxLen = 0
    for i in range(len(s)):
        map = {}
        for j in range(i,len(s)):
            if s[j] not in map:
                map[s[j]] = 1
            else:
                break
            maxLen = max(maxLen,len(map))         
    return maxLen
# print(LongestSubstringWithoutRepeatingCharacters("abcddabac"))

# Optimal Aproach :
def LongestSubstringWithoutRepeatingCharactersOptimal(s):
    maxLen = 0
    l = 0
    charSet = set()
    for r in range(len(s)):
        while s[r] in charSet:
            set.remove(s[l])
            l += 1
        charSet.add(s[r])
        maxLen = max(maxLen,r-l+1)
    return maxLen
# print(LongestSubstringWithoutRepeatingCharactersOptimal("abcddabac"))
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 2 : Max Consecutive Ones III
# Brute force :
def MaxConsecutiveOnesKflips(inArr,k):
    maxlen = 0
    for i in range(len(inArr)):
        z = 0
        for j in range(i,len(inArr)):
            if inArr[j] == 0:
                z += 1
            if z > k:
                break
            maxlen = max(maxlen,j-i+1)
    return maxlen
# print(MaxConsecutiveOnesKflips([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0],3))

# Better aproach :
def MaxConsecutiveOnesKflipsBetter(inArr,k):
    maxlen = 0
    l = 0
    z = 0
    for r in range(len(inArr)):
        if inArr[r] == 0:
            z += 1
        while z > k:
            if inArr[l] == 0:
                z -= 1
            l += 1
        maxlen = max(maxlen,r-l+1)
    return maxlen
# print(MaxConsecutiveOnesKflipsBetter([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0],3))

# Optimal aproach :
def MaxConsecutiveOnesKflipsOptimal(inArr,k):
    maxlen = 0
    l = 0
    z = 0
    for r in range(len(inArr)):
        if inArr[r] == 0:
            z += 1
        if z > k:
            if inArr[l] == 0:
                z -= 1
            l += 1
        maxlen = max(maxlen,r-l+1)
    return maxlen
# print(MaxConsecutiveOnesKflipsOptimal([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0],3))
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 3 : Fruit Into Baskets
def FruitIntoBaskets(inArr):
    maxFruits = 0
    for i in range(len(inArr)):
        fruitSet = set()
        for j in range(i,len(inArr)):
            fruitSet.add(inArr[j])
            if len(fruitSet) <= 2:
                maxFruits = max(maxFruits,j-i+1)
            else:
                break
    return maxFruits
# print(FruitIntoBaskets([1, 2, 3, 2, 2]))

# Better approach :
# from collections import defaultdict
def FruitIntoBasketsBetter(inArr):
    fruitTrack = {}
    maxFruits = 0
    l = 0
    for r in range(len(inArr)):
        if inArr[r] in fruitTrack:
            fruitTrack[inArr[r]] += 1
        else:
            fruitTrack[inArr[r]] = 1
        if len(fruitTrack) > 2: # we can use 'while' as well
            fruitTrack[inArr[l]] -= 1
            if fruitTrack[inArr[l]] == 0:
                del fruitTrack[inArr[l]]
            l += 1
        maxFruits = max(maxFruits,r-l+1)
    return maxFruits
# print(FruitIntoBasketsBetter([1, 2, 3, 2, 2]))
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 4 : Longest Repeating Character Replacement
# Brute force :
def LongestRepeatingCharacterReplacement(s,k):
    maxLen = 0
    for i in range(len(s)):
        hashFreq = [0]*26
        maxFreq = 0
        for j in range(i,len(s)):
            hashFreq[ord(s[j])-ord('A')] += 1
            maxFreq = max(maxFreq,hashFreq[ord(s[j])-ord('A')])
            windowLen = j-i+1
            charReplace = windowLen - maxFreq
            if charReplace <= k:
                maxLen = max(maxLen,j-i+1)
            else:
                break
    return maxLen
# print(LongestRepeatingCharacterReplacement('BAABAABBBAAA',2))

def LongestRepeatingCharacterReplacement(s,k):
    maxLen = 0
    for i in range(len(s)):
        hashFreq = {}
        maxFreq = 0
        for j in range(i,len(s)):
            hashFreq[s[j]] = hashFreq.get(s[j],0)+1
            maxFreq = max(maxFreq,hashFreq[s[j]])
            windowLen = j-i+1
            charReplace = windowLen - maxFreq
            if charReplace <= k:
                maxLen = max(maxLen,j-i+1)
            else:
                break
    return maxLen
LongestRepeatingCharacterReplacement('babba',1)

# Better approach :
def LongestRepeatingCharacterReplacementBetter(s,k):
    maxLen = 0
    hashFreq = {}
    l = 0
    maxFreq = 0
    for r in range(len(s)):
        hashFreq[s[r]] = hashFreq.get(s[r],0)+1
        maxFreq = max(maxFreq,hashFreq[s[r]])
        if r-l+1 - maxFreq > k: # we can use 'while'
            hashFreq[s[l]] -= 1
            l += 1
        maxLen = max(maxLen,r-l+1)
    return maxLen
# print(LongestRepeatingCharacterReplacementBetter('BAABAABBBAAA',2))
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 5 : Binary Subarrays With Sum
# Brute force :
def BinarySubarraysSumK(inArr,k):
    count = 0
    for i in range(len(inArr)):
        sum = 0
        for j in range(i,len(inArr)):
            sum += inArr[j]
            if sum == k:
                count += 1
    return count
# print(BinarySubarraysSumK([1, 0, 1, 0, 1],2))

# Better approach :
def BinarySubarraysSumKBetter(inArr,k):
    count = 0
    hashPrefixSum = {0:1}
    currentSum = 0
    for i in inArr:
        currentSum += i
        targetPrefix = currentSum - k
        if targetPrefix in hashPrefixSum:
            count += hashPrefixSum[targetPrefix]
        hashPrefixSum[currentSum] = hashPrefixSum.get(currentSum,0)+1
    return count
# print(BinarySubarraysSumKBetter([1, 0, 1, 0, 1],2))

# Optimal approach :
def BinarySubarraysSumKOptimal(inArr,k):
    def SumAtMostK(n):
        if n < 0:
            return 0
        count = 0
        l = 0
        sum = 0
        for r in range(len(inArr)):
            sum += inArr[r]
            while sum > n:
                sum -= inArr[l]
                l += 1
            count += r-l+1
        return count
    return SumAtMostK(k) - SumAtMostK(k-1)
# print(BinarySubarraysSumKOptimal([1, 0, 1, 0, 1],2))
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 6 : Count number of Nice subarrays
def NiceSubarrays(inArr,k):
    count = 0
    for i in range(len(inArr)):
        oddcount = 0
        for j in range(i,len(inArr)):
            if inArr[j]%2 != 0:
                oddcount += 1
            if oddcount > k:
                break
            if oddcount == k:
                count += 1
    return count
# print(NiceSubarrays([1, 1, 2, 1, 1] , k = 3))

# Failed approach :
def NiceSubarraysBetter(inArr,k):
    count = 0
    l = 0
    oddcount = 0
    for r in range(len(inArr)):
        if inArr[r]%2 != 0:
            oddcount += 1
        while oddcount > k:
            if inArr[l]%2 != 0:
                oddcount -= 1
            l+=1
        if oddcount == k:
            count += r-l+1
    return count
# print(NiceSubarraysBetter([1, 1, 2, 1, 1] , k = 3))

# Optimal approach : consider 1 as odd and 0 as even
def NiceSubarraysOptimal(inArr,k):
    def SumAtMostK(n):
        if n < 0:
            return 0
        count = 0
        l = 0
        sum = 0
        for r in range(len(inArr)):
            sum += inArr[r]%2
            while sum > n:
                sum -= inArr[l]%2
                l += 1
            count += r-l+1
        return count
    return SumAtMostK(k) - SumAtMostK(k-1)
# print(NiceSubarraysOptimal([1, 1, 2, 1, 1] , k = 3))
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 7 : Number of Substrings Containing All Three Characters
# Brute force :
def AllThreeCharactersSubstrings(s):
    count = 0
    for i in range(len(s)):
        mp = {'a':0,'b':0,'c':0}
        for j in range(i,len(s)):
            mp[s[j]] += 1
            if mp['a']>0 and mp['b']>0 and mp['c']>0:
                count += 1
    return count
# print(AllThreeCharactersSubstrings("abcba"))

# Better approach :
def AllThreeCharactersSubstringsBetter(s):
    count = 0
    l = 0
    hmap = {}
    for r in range(len(s)):
        if s[r] not in hmap:
            hmap[s[r]] = 1
        else:
            hmap[s[r]] += 1
        while len(hmap) == 3:
            count += len(s) - r
            hmap[s[l]] -= 1
            if hmap[s[l]] == 0:
                del hmap[s[l]]
            l+=1
    return count
# print(AllThreeCharactersSubstringsBetter("abcba"))
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 8 : Maximum Points You Can Obtain from Cards
# Brute force :
def MaximumPointsObtainfromCards(inArr,k):
    maxSum = 0
    for i in range(k+1):
        sum = 0
        for j in range(i):
            sum += inArr[j]
        for j in range(k-i):
            sum += inArr[len(inArr)-1-j]
        maxSum = max(maxSum,sum)
    return maxSum
# print(MaximumPointsObtainfromCards([1, 2, 3, 4, 5, 6, 1],3))

# Optimal approach :
def MaximumPointsObtainfromCardsOptimal(inArr,k):
    maxSum = 0
    leftSum = 0
    rightSum = 0
    for i in range(k):
        leftSum += inArr[i]
        maxSum = leftSum
    rightIndex = len(inArr) - 1
    for i in range(k,-1,-1):
        leftSum -= inArr[i]
        rightSum += inArr[rightIndex]
        rightIndex -= 1
    maxSum = max(maxSum,leftSum+rightSum)
    return maxSum
# print(MaximumPointsObtainfromCardsOptimal([1, 2, 3, 4, 5, 6, 1],3))
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
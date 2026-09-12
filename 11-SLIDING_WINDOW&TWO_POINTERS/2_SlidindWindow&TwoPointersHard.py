# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 1 : Longest Substring With At Most K Distinct Characters
# Brute force :
def LongestSubstringAtMostKDistinctCharacters(s,k):
    maxLen = 0
    for i in range(len(s)):
        freqMap = {}
        for j in range(i,len(s)):
            freqMap[s[j]] = freqMap.get(s[j],0)+1
            if len(freqMap) > k:
                break
            maxLen = max(maxLen,j-i+1)
    return maxLen
# print(LongestSubstringAtMostKDistinctCharacters(s = "aababbcaacc" , k = 2))

# Optimal approach :
def LongestSubstringAtMostKDistinctCharactersOptimal(s,k):
    maxLen = 0
    freqMap = {}
    l = 0
    for r in range(len(s)):
        freqMap[s[r]] = freqMap.get(s[r],0)+1
        while len(freqMap) > k:
            freqMap[s[l]] -= 1
            if freqMap[s[l]] == 0:
                del freqMap[s[l]]
            l += 1
        maxLen = max(maxLen,r-l+1)
    return maxLen
# print(LongestSubstringAtMostKDistinctCharactersOptimal(s = "aababbcaacc" , k = 2))
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 2 : Subarrays with K Different Integers
# Brute force :
def SubarrayswithKDifferentIntegers(inArr,k):
    count = 0
    for i in range(len(inArr)):
        FreqMap = {}
        for j in range(i,len(inArr)):
            FreqMap[inArr[j]] = FreqMap.get(inArr[j],0)+1
            if len(FreqMap) == k:
                count+=1
            if len(FreqMap) > k:
                break
    return count
# print(SubarrayswithKDifferentIntegers([1, 2, 1, 2, 3],2))

# Optimal approach :
def SubarrayswithKDifferentIntegersOptimal(inArr,k):
    def atMostK(n):
            if n < 0:
                return 0
            count = 0
            FreqMap = {}
            l = 0
            for r in range(len(inArr)):
                FreqMap[inArr[r]] = FreqMap.get(inArr[r],0)+1
                while len(FreqMap) > n:
                    FreqMap[inArr[l]] -= 1
                    if FreqMap[inArr[l]] == 0:
                        del FreqMap[inArr[l]]
                    l+=1
                count += r-l+1
            return count
    return atMostK(k)-atMostK(k-1)
# print(SubarrayswithKDifferentIntegersOptimal([1, 2, 1, 2, 3],2))
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 3 : Minimum Window Substring
# Brute force :
def MinimumWindowSubstring(s,t):
    n = len(s)
    m = len(t)
    if n < m or m == 0:
        return ""
    minIndex = float('inf')
    startIndex = -1
    for i in range(n):
        # Step 1: Fresh frequency map for each starting position i
        FreqMap = {}
        # Step 2: Expand j strictly from i to n-1
        for j in range(m):
            FreqMap[t[j]] = FreqMap.get(t[j],0)+1
        count = 0
        for j in range(i,n):
            # if FreqMap[s[j]] > 0:
            #     count += 1
            # If s[j] is needed, count it
            if FreqMap.get(s[j],0) > 0:
                count +=1
            # Decrement frequency count
            FreqMap[s[j]] = FreqMap.get(s[j],0)-1
                # FreqMap[s[j]] -= 1
            # Step 3: When all characters of t are found
            if count == m:
                if j-i+1 < minIndex:
                    minIndex = j-i+1
                    startIndex = i
                    break # Expanding further from this 'i' only yields longer windows
    return "" if startIndex == -1 else s[startIndex:startIndex + minIndex]
# print(MinimumWindowSubstring('ddaaabbca','abc'))

# Optimal approach :
def MinimumWindowSubstringOptimal(s,t):
    n = len(s)
    m = len(t)
    if n < m or m == 0:
        return ""
    # Frequency map for t
    FreqMap = {}
    for ch in t:
        FreqMap[ch] = FreqMap.get(ch,0)+1
    minIndex = float('inf')
    startIndex = -1
    l = 0
    count = 0
    for r in range(n):
        # Step 1: Expand right pointer
        if FreqMap.get(s[r],0) > 0:
            count += 1
        FreqMap[s[r]] = FreqMap.get(s[r],0)-1
        # Step 2: When window contains all characters, shrink from left
        while count == m:
            # Update minimum window found so far
            if r-l+1 < minIndex:
                minIndex = r-l+1
                startIndex = l
            # Remove s[l] from window
            FreqMap[s[l]] += 1
            if FreqMap[s[l]] > 0:
                count -= 1
            l += 1
    return "" if startIndex == -1 else s[startIndex:startIndex+minIndex]
# print(MinimumWindowSubstringOptimal('ddaaabbca','abc'))
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# PROBLEM 4 : Minimum Window Subsequence
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
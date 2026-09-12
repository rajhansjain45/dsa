# PROBLEM 1 : Sort Characters By Frequency - Given a string s, sort it in decreasing order based on the frequency of characters, and return the sorted string.
# Brute force : count the frequency of each character and sort the characters based on their frequency.
def SortCharactersByFrequency(s):
    frequency = {}
    for c in s:
        frequency[c] = frequency.get(c,0) + 1
    SortedChars = sorted(frequency.keys(), key=lambda x: frequency[x], reverse=True)
    result = ''
    for char in SortedChars:
        result += char * frequency[char]
    return result
# print(SortCharactersByFrequency('tree'))  # Output: "eert"

# Optimal approach : use a bucket sort to sort the characters based on their frequency.
def SortCharactersByFrequencyOptimal(s):
    frequency = {}
    for c in s:
        frequency[c] = frequency.get(c,0) + 1
    buckets = [[] for _ in range(len(s) + 1)]
    for char, freq in frequency.items():
        buckets[freq].append(char)
    result = ''
    for i in range(len(buckets) - 1, 0, -1):
        for char in buckets[i]:
            result += char * i
    return result

# ----------------------------------------------------------------------------------
# PROBLEM 2 : Maximum Nesting Depth of the Parentheses
def MaxNestingDepth(s):
    MaxDepth = 0
    CurrentDepth = 0
    for ch in s:
        if ch == '(':
            CurrentDepth +=1
        elif ch == ')' : 
            CurrentDepth -= 1
        MaxDepth = max(MaxDepth, CurrentDepth)
    return MaxDepth
# print(MaxNestingDepth("(1+(2*3)+((8)/4))+1"))  # Output: 3

# ----------------------------------------------------------------------------------
# PROBLEM 3 : Roman Numerals to Integer
def RomanToInt(s):
    RomanMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(len(s)-1):
        if RomanMap[s[i]] < RomanMap[s[i+1]]:
            total -= RomanMap[s[i]]
        else:
            total += RomanMap[s[i]]
    total += RomanMap[s[-1]]
    return total
# print(RomanToInt("MCMXCIV"))  # Output: 1994

# Variation : Integer to Roman
def IntToRoman(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_num = ''
    for i in range(len(val)):
        count = num // val[i]
        roman_num += syms[i] * count
        num -= val[i] * count
    return roman_num
# print(IntToRoman(1994))  # Output: "MCMXCIV"

# ----------------------------------------------------------------------------------
# PROBLEM 4 : String to Integer (atoi)
# Brute force:
def StringToInteger(s):
    s = s.lstrip()
    i = 0
    if not s:
        return 0
    sign = 1

    if s[0] in ['-','+']:
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1
    result = 0
    while i < len(s) and s[i].isdigit():
        result = result*10 + int(s[i])
        i += 1
    result *= sign

    if result < -2**31:
        return -2**31
    elif result > 2**31 - 1:
        return 2**31 - 1

    return result
# print(StringToInteger("   -42"))  # Output: -42

# Optimal approach : using Recursion
def Helper(s, index, CurrNum, sign):
    if index >= len(s) or not s[index].isdigit():
        return CurrNum * sign
    CurrNum = CurrNum * 10 + int(s[index])
    return Helper(s, index + 1, CurrNum, sign)

def RecursiveAtoI(s):
    s = s.lstrip()
    if not s:
        return 0
    sign = 1
    Index = 0
    if s[0] in ['-','+']:
        sign = -1 if s[0] == '-' else 1
        Index += 1
    result = Helper(s, Index, 0, sign)
    if result < -2**31:
        return -2**31
    elif result > 2**31 - 1:
        return 2**31 - 1
    return result
# print(RecursiveAtoI("   -42"))  # Output: -42

# ----------------------------------------------------------------------------------
# PROBLEM 5 :  number of substrings that contain exactly k distinct characters.
# Brute force : generate all possible substrings of the string, count the number of distinct characters in each substring 
# and keep track of the count of substrings that contain exactly k distinct characters.
def SubstringsWithKDistinct(s, k):
    count = 0
    countDistinct = {}
    for i in range(len(s)):
        countDistinct.clear()
        for j in range(i, len(s)):
            countDistinct[s[j]] = countDistinct.get(s[j], 0) + 1
            if len(countDistinct) == k:
                count += 1
            elif len(countDistinct) > k:
                break
    return count
# print(SubstringsWithKDistinct("pqpqs", 2))  # Output: 7

# Optimal approach : using sliding window and two pointers
def SubstringsWithAtMostKDistinct(s,k):
    count = 0
    hashmap = {}
    left = 0 
    right = 0
    while right < len(s):
        hashmap[s[right]] = hashmap.get(s[right], 0) + 1
        while len(hashmap) > k:
            hashmap[s[left]] -= 1
            if hashmap[s[left]] == 0:
                del hashmap[s[left]]
            left += 1
        count += right - left + 1
        right += 1
    return count

def SubstringsWithKDistinctOptimal(s,k): 
    return SubstringsWithAtMostKDistinct(s,k) - SubstringsWithAtMostKDistinct(s,k-1)

# print(SubstringsWithKDistinctOptimal("pqpqs", 2))  # Output: 7

# ----------------------------------------------------------------------------------
# PROBLEM 6 : Longest Palindromic Substring
# Brute force : generate all possible substrings of the string, check if they are palindromes and keep track of the longest one.
def LongestPalindromeBruteForce(s):
    def isPalindrome(sub):
        return sub == sub[::-1]
    
    longest = ''
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if isPalindrome(substring) and len(substring) > len(longest):
                longest = substring
    return longest
# print(LongestPalindromeBruteForce("babad"))  # Output: "aba" or "bab"

# optimal approach : using expand around center technique
def LongestPalindromeOptimal(s):
    result = ''
    resultLength = 0
    def expandAroundCenter(left, right):
        nonlocal result, resultLength
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > resultLength:
                result = s[left:right+1]
                resultLength = right - left + 1
            left -= 1
            right += 1
    
    for i in range(len(s)):
        # for odd length (centre is at i)
        expandAroundCenter(i,i)

        # for even length (centre is between i and i+1)
        expandAroundCenter(i,i+1)
    
    return result
# print(LongestPalindromeOptimal("babad"))  # Output: "aba" or "bab"

# Breaking above code in two differnt funtions for better readability
def ExpandArountCenter(string,left,right):
    while left >= 0 and right < len(string) and string[left] == string[right]:
        left -= 1
        right += 1
    # Why s[left+1 : right]? 
    # When the loop breaks, s[left] and s[right] are NOT matching.
    # We need the characters between them.
    return string[left+1:right]

def LongestPalindromeOptimal2(s):
    result = ''
    for i in range(len(s)):
        # for odd length (centre is at i)
        oddPalindrome = ExpandArountCenter(s,i,i)

        # for even length (centre is between i and i+1)
        evenPalindrome = ExpandArountCenter(s,i,i+1)

        longestPalindrome = oddPalindrome if len(oddPalindrome) > len(evenPalindrome) else evenPalindrome
        if len(longestPalindrome) > len(result):
            result = longestPalindrome
    return result
# print(LongestPalindromeOptimal2("babad"))  # Output: "aba" or "bab"

# ----------------------------------------------------------------------------------
# PROBLEM 7 : Sum of Beauty of All Substrings.
def SubstringsBeautySum(s):
    totalBeauty = 0
    for i in range(len(s)):
        freq = {}
        for j in range(i,len(s)):
            freq[s[j]] = freq.get(s[j],0) + 1
            maxFreq = max(freq.values())
            minFreq = min(freq.values())
            totalBeauty += maxFreq - minFreq
    return totalBeauty
# print(SubstringsBeautySum("aabcb"))  # Output: 5

# ----------------------------------------------------------------------------------
# PROBLEM 8 : Reverse every word in a string.
# as saame as the PROBLEM 2.
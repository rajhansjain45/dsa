# PROBLEM 1 : Remove outermost parantheses - given a string of parantheses, remove the outermost parantheses from each primitive string. 
# A primitive string is a non-empty string that cannot be partitioned into two non-empty valid parentheses strings.
def RemoveOuterParentheses(s):
    stack = []
    result = ""
    level = 0
    for char in s:
        if char == '(':
            if level > 0:
                result += char
            level += 1
        else:
            level -= 1
            if level > 0:
                result += char
    # for char in s:
    #     if char == '(':
    #         if stack:  # If stack is not empty, add '(' to result
    #             result += char
    #         stack.append(char)  # Push '(' onto the stack
    #     else:  # char == ')'
    #         stack.pop()  # Pop the last '(' from the stack
    #         if stack:  # If stack is not empty, add ')' to result
    #             result += char
    return result
# print(RemoveOuterParentheses("(()())(())(()(()))"))  # Output: "()()()()(())"

# ----------------------------------------------------------------------------------
# PROBLEM 2 : Reverse words in a string - Given a string, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
# Example: Input: "Hello World" Output: "World Hello"
# brute force : manually split the string into words, reverse the list of words and join them back together.
def ReverseWordsInAString(s):
    WordsList = []
    word = ""
    for char in s:
        if char != ' ':
            word += char
        else:
            WordsList.append(word)
            word = ""
    # to handle the last word in the string, if there is one
    if word:
        WordsList.append(word)
    WordsList.reverse()
    return ' '.join(WordsList)
# print(ReverseWordsInAString("Hello World"))  # Output: "World Hello"

# Better approach : use built-in functions to split the string into words, reverse the list of words and join them back together.
def ReverseWordsInAStringBuiltin(s):
    WordsList = s.split()
    WordsList.reverse()
    return ' '.join(WordsList)
# print(ReverseWordsInAStringBuiltin("Hello World"))  # Output: "World Hello"

# Optimal aproach : using right to left pointer
def ReverseWordsInAStringOptimal(s):
    result = ''
    i = len(s) - 1
    while i >= 0:
        while i >= 0 and s[i] == ' ':
            i -= 1
        if i < 0:
            break

        j = i
        while i >= 0 and s[i] != ' ':
            i -= 1

        word = s[i+1:j+1]
        if result != '':
            result += ' '
        result += word
    return result 
    #     result += s[i + 1:j + 1] + ' '
    # return result.strip()
         
# print(ReverseWordsInAStringOptimal("Hello World"))  # Output: "World Hello"

# -----------------------------------------------------------------------------------
# PROBLEM 3 : Largest odd number in a string - Given a string containing digits, return the largest odd number
#  that can be formed by substring of the string. If no odd number can be formed, return an empty string.
# brute force : generate all possible substrings of the string, check if they are odd numbers and keep track of the largest one.
def LargestOddNumberInAStringBruteForce(s):
    LargestOdd = ''
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if int(substring[-1]) % 2 == 1:
                # compare numerically
                if len(substring) > len(LargestOdd):
                    LargestOdd = substring
                elif len(substring) == len(LargestOdd) and substring > LargestOdd:
                    LargestOdd = substring

    return LargestOdd
# print(LargestOddNumberInAStringBruteForce("354276"))  # Output: "35427"

# Optimal aproach : finding first odd from the end
def LargestOddNumberInAString(s):
    LargestOdd = ''
    for i in range(len(s),-1,-1):
        if i < len(s) and int(s[i]) % 2 == 1:
            LargestOdd = s[:i+1]
            break
    return LargestOdd
# print(LargestOddNumberInAString("354276"))  # Output: "35427"

# -----------------------------------------------------------------------------------
# PROBLEM 4 : Longest common prefix - Given an array of strings, find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Optimal approach : sort the array of strings and compare the first and last strings in the sorted array to find the longest common prefix.
def LongestCommonPrefix(strs):
    if not strs:
        return ''
    strs.sort()
    first = strs[0]
    last = strs[-1]
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return first[0:i]
    return " "
# print(LongestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"

# -----------------------------------------------------------------------------------
# PROBLEM 5 : Isomorphic Strings - Given two strings s and t, determine if they are isomorphic. 
# Two strings are isomorphic if the characters in s can be replaced to get t.
def IsomorphicStrings(s,t):
    mapS = [0]*256
    mapT = [0]*256
    for i in range(len(s)):
        charS = ord(s[i])
        charT = ord(t[i])
        if mapS[charS] == mapT[charT]:
            mapS[charS] = i+1
            mapT[charT] = i+1
        else :
            return False
    return True

# print(IsomorphicStrings('foo','bar'))

# -----------------------------------------------------------------------------------
# PROBLEM 6 : Check if one string is rotation of another - move a[0] to last and check till found else false
# Brute force : find all rotations and check
def CheckRotation(string , target):
    for i in range(len(string)):
        # generating rotated versions of string
        rotated = string[i:] + string[:i]
        if rotated == string:
            return True
    return False
# print(CheckRotation('rotation','tionrota'))

# Optimal approach : check if target is a substring of string + string
def CheckRotationOptimal(string , target):
    DoubledString = string + string
    return target in DoubledString
# print(CheckRotationOptimal('rotation','tionrota'))

# -----------------------------------------------------------------------------------
# PROBLEM 7 : Valid Anagram - Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Brute force : sort both strings and compare
def ValidAnagram(s,t):
    return sorted(s) == sorted(t)
# print(ValidAnagram('anagram','nagaram'))  # Output: True

# Optimal approach : use a hash map to count the frequency of each character in both strings and compare the counts.
def ValidAnagramOptimal(s,t):
    if len(s) != len(t):
        return False
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1
    return True
# print(ValidAnagramOptimal('anagram','nagaram'))  # Output: True

# -----------------------------------------------------------------------------------
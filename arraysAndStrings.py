# determines if a string has all unique characters
def isUnique(s):
    seen = set()
    for i in range(len(s)):
        if (s[i] in seen):
            return False
        else:
            seen.add(s[i])
    return True

# checks if one is a permutation of the other.
def checkPermutation(s1, s2):
    if len(s1) != len(s2):
        return False
    # count characters in s1 and add to dict
    words = dict()
    for i in range(len(s1)):
        if s1[i] in words:
            words[s1[i]] += 1
        else:
            words[s1[i]] = 1
    
    # remove character counts from dict if they are in s2
    for i in range(len(s2)):
        if s2[i] not in words:
            return False
        if words[s2[i]] < 1:
            return False
        words[s2[i]] -= 1
    
    # if s1's characters were equal to s2's, words dict should be empty
    for key in words.keys():
        if words[key] != 0:
            return False
    
    # passed all tests, it is a permutation
    return True

# replaces all spaces in a string with '%20'.
def URLify(s,n):
    newS = ""
    for i in range(n):
        if (s[i] == " "):
            newS += "%20"
        else:
            newS += s[i]
    return newS

# makes all combinations with string s and character c
def makePermutations(s, c):
    words = []
    for i in range(len(s)):
        word = s[:i] + c + s[i:]
        words.append(word)
    return words

# checks if s is the same when reversed
def isPalindrome(s):
    reversedS = ""
    for i in range(len(s)):
        reversedS += s[len(s) - i - 1]
    return reversedS == s

# Given a string, checks if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
def palindromePermutation(s):
    # make permutations of s
    for i in range(len(s)):
        new = s[:i] + s[i+1:]
        words = makePermutations(new,s[i])
        for word in words:
            if (checkPermutation(s, word) and isPalindrome(word)):
                return True
    return False

# There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, checks if they are
# one edit (or zero edits) away.
def oneAway(s1, s2):
    word1 = "" # does not change
    word2 = "" # the one we need to alter
    count = 0

    # initialize
    if s1 == s2:
        return count
    elif len(s1) > len(s2):
        word1 = s1
        word2 = s2
    else:
        word1 = s2
        word2 = s1
    i = 0
    j = 0
    while (i < len(word2) and j < len(word1)):
        # compare letters
        if word1[j] != word2[i]:
            count += 1
            if (len(s1) == len(s2)):
                i += 1
        else:
            i += 1
        j += 1
        
        if count > 1:
            return False

    # if not seen all of word1
    if (j < len(word1)):
        count += len(word2) - len(word1)
    return count <= 1
    
# Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3.
def compressString(s):
    if (len(s) == 0):
        return s
    count = 1
    prev = s[0]
    newS = s[0]
    for i in range(1, len(s)):
        if (s[i] == prev):
            count += 1
        else:
            newS += str(count)
            count = 1
            newS += s[i]
            prev = s[i]
    newS += str(count)
    
    if (len(newS) > len(s)):
        return s
    return newS

# Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
def rotateMatrix(matrix):
    # initialize resulting matrix
    newMatrix = []
    for i in range(len(matrix)):
        newMatrix.append([])

    # append to new matrix
    # start from the last row, up the rows on columns
    # add those items to first row
    for c in range(len(matrix)):
        for r in range(len(matrix)-1, -1, -1):
            newMatrix[c].append(matrix[r][c])
    del matrix
    return newMatrix

# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.
def zeroMatrix(matrix):
    zeroPositions = []
    rows = len(matrix)
    columns = len(matrix)
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if (matrix[r][c] == 0):
                zeroPositions.append((r,c))
    for pos in range(len(zeroPositions)):
        r = zeroPositions[pos][0]
        c = zeroPositions[pos][1]
        for i in range(rows):
            if (i == r): 
                for j in range(columns):
                    matrix[i][j] = 0
            else:
                matrix[i][c] = 0
    
    del zeroPositions
    return matrix

# checks if s2 is a substring of s1
def isSubstring(s1, s2):
    i = 0
    j = 0
    while (i < len(s1) and j < len(s2)):
        if (s1[i] == s2[j]):
            i += 1
            j += 1
        else:
            j = 0
            i += 1
    
    if (j == len(s2)):
        return True
    return False

# Assume you have a method isSubstring which checks if one word is a substring
# of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 
# using only one call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").
def rotateString(s1, s2):
    if (len(s1) != len(s2)):
        return False

    for i in range(len(s1)):
        print(s1, s2, i)
        if s2 == s1:
            return True
        s2 = s2[1:] + s2[0]
        
    return isSubstring(s1,s2)

def longestStringPalindrome(s1):
    if (s1 == ""):
        return ""
    if (isPalindrome(s1)):
        return s1
    
    result1 = longestStringPalindrome(s1[1:])
    result2 = longestStringPalindrome(s1[:-1])

    if (len(result1) > len(result2)):
        return result1
    return result2

if __name__ == '__main__':
    print("Testing isUnique...")
    assert(isUnique("abcd") == True)
    assert(isUnique("abbcd") == False)
    assert(isUnique("catat") == False)
    assert(isUnique("bat") == True)
    print("Passed")

    print("Testing checkPermutation...")
    assert(checkPermutation("cat", "tac") == True)
    assert(checkPermutation("boot", "toob") == True)
    assert(checkPermutation("taboo", "capoo") == False)
    assert(checkPermutation("cab", "bato") == False)
    print("Passed")

    print("Testing URLify...")
    assert(URLify("hey you are", 11) == "hey%20you%20are")
    print("Passed")

    print("Testing palindromePermutations...")
    assert(palindromePermutation("toot") == True)
    assert(palindromePermutation("act") == False)
    print("Passed")

    print("Testing oneAway...")
    assert(oneAway("pale", "ple") == True)
    assert(oneAway("pales", "pale") == True)
    assert(oneAway("pale", "bale") == True)
    assert(oneAway("pale", "bake") == False)
    print("Passed")

    print("Testing compressString...")
    assert(compressString("aabcccccaaa") == "a2b1c5a3")
    assert(compressString("aabccccca") == "a2b1c5a1")
    assert(compressString("aa") == "a2")
    assert(compressString("") == "")
    assert(compressString("abc") == "abc")
    print("Passed")

    print("Testing rotateMatrix...")
    assert(rotateMatrix([[0,1,2],[3,4,5],[6,7,8]]) == [[6,3,0], [7,4,1], [8,5,2]])
    print("Passed")

    print("Testing zeroMatrix...")
    assert(zeroMatrix([[0,1],[2,3]]) == [[0,0],[0,3]])
    assert(zeroMatrix([[0,1, 2],[3,4,5],[6,0,8]]) == [[0,0,0],[0,0,5],[0,0,0]])
    print("Passed")

    print("Testing rotateString...")
    # print(rotateString("erbottlewat", "waterbottle"))
    assert(rotateString("erbottlewat", "waterbottle") == True)
    print("Passed")

    print("Testing longestStringPalindrome...")
    assert(longestStringPalindrome("racecarbee") == "racecar")
    assert(longestStringPalindrome("bobracecar") == "racecar")
    assert(longestStringPalindrome("eeobraecac") == "cac")
    print("Passed")




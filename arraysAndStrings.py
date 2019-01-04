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

# Write a method to replace all spaces in a string with '%20'.
def URLify(s,n):
    newS = ""
    for i in range(n):
        if (s[i] == " "):
            newS += "%20"
        else:
            newS += s[i]
    return newS

# make all combinations with string s and character c
def makePermutations(s, c):
    words = []
    for i in range(len(s)):
        word = s[:i] + c + s[i:]
        words.append(word)
    return words

# check if s is the same when reversed
def isPalindrome(s):
    reversedS = ""
    for i in range(len(s)):
        reversedS += s[len(s) - i - 1]
    return reversedS == s

def palindromePermutation(s):
    # make permutations of s
    for i in range(len(s)):
        new = s[:i] + s[i+1:]
        print(new)
        words = makePermutations(new,s[i])
        for word in words:
            if (checkPermutation(s, word) and isPalindrome(word)):
                print(isPalindrome(word))
                return True
    return False

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

    print("Testing URLify")
    assert(URLify("hey you are", 11) == "hey%20you%20are")
    print("Passed")

    print("Testing palindromePermutations")
    print(palindromePermutation("toot"))
    assert(palindromePermutation("toot") == True)
    assert(palindromePermutation("act") == False)
    print("Passed")

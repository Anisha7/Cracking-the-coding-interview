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

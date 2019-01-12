
# def makeUnique(givenStr):
#     # given string
#     myStr = ""
#     mySet = set()

#     for char in givenStr:
#         # if current item is in the set, don't add it to myStr
#         if char not in mySet:
#             myStr += char
#             mySet.add(char)
#     print(myStr)
#     return myStr

# makeUnique("aabbcccc")

# remove x from list l
def removeOccurences(l, x):
    # x = b
    # l = [a,b,b,d]
    # i = 0, l[i] == b? not => i += 1
    # i = 1, l[1] == b? yes => remove b
        # l[:1] + l[2:] : [a] + [c,d] = [a,c,d]
        # l = [a,b,d], i = 1



    # for i in range(len(l))
    i = 0
    while (i<len(l)):
        # if l[i] is x, remove it
        if l[i] == x:
            # l.pop(i)
            l = l[:i] + l[i + 1:]
        # if not, add 1 to i
        else:
            i += 1
    print(l)
    return l

removeOccurences(["a","b","b","c","d","d"], "b")
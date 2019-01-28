def substring(s):
    max_count = 0
    start_index = 0
    dict_of_letters = {}
    for idx,x in enumerate(s):
        if x in dict_of_letters:
            print(x)
            #finding index of previous occuring letter
            letter_index = dict_of_letters[x]
            #moving start index to the right
            start_index = letter_index + 1
            #getting the count of current substring
            count = idx - start_index
            print("string: ", s[start_index:idx + 1])
            print("count: ", count)
        #if letter isn't in dictionary 
        else:
            print("I made it here")
            dict_of_letters[x] = idx
            count = idx - start_index
        
        if count > max_count:
            max_count = count
    return max_count

print(substring('adbcaea'))
        
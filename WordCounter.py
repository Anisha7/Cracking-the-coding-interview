# Implement a program that counts occurrences of words in a given file.
# The input will have mul ple lines, with each line containing one or more words. 
# The output will be each word and how many  mes it appears. 
# You should print each word and its count on a separate line. 
# The output should sort the words in lexicographically sorted order.

import sys
import os.path

# data = sys.stdin.readlines()
# print "Counted", len(data), "lines."

def WordCounter(file): # O(N) where N = # of words in the file, 
    #m*n = N where m is # of words in a line and n is # of lines in file
    data = file
    d = dict() # store counts
    if (os.path.isfile(file)):
        # if its a file, read it into data
        stuff = open(file,'r')
        data = stuff.read()

    # read each line and get counts for its words
    for line in data.splitlines(): # O(n*m) where n = lines in the file
        words = line.split()
        for word in words: # O(m) where m = words in a line
            word = word.lower()
            if (d.get(word) != None):
                d[word] += 1
            else:
                d[word] = 1
    
    # print counts
    for key in d.keys():
        print('"%s" occurs %d times\n'%(key, d[key]))
    return
    

print(WordCounter("hi there you.\n Hi you\n"))
print(WordCounter('linkedLists.py'))
# 1. Write a function to swap a number in place (that is, without temporary variables).
def numberSwapper(A, i, j):
    A[i],A[j] = A[j], A[i] 

# 2. Design a method to find the frequency of occurrences of any given word in a
# book. What if we were running this algorithm multiple times?
def wordFrequencies(book, word):
    d = dict()
    for w in book.split():
        w = "".join(c for c in w if c not in ('!','.',':'))
        if (d.get(w) > -1) :
            d[w] += 1
        else:
            d[w] = 0
    
    return d[word]

# 3. Given two straight line segments (represented as a start point and an end point),
# compute the point of intersection, if any.
def intersection(line1, line2):


# 4. Design an algorithm to figure out if someone has won a game of 3x3 tic-tac-toe.
def ticTacWin(board):
    # invalid board
    if (len(board) != 3):
        return False
    # check diagonal with top left(forward down) and top right(backward down)
    if (board[0][0] != -1):
        if (board[0][0] == board[1][1] and board[0][0] == board[2][2]):
            return True
    for r in range(len(board)):
        # check right
        if (board[r][0] != -1):
            if (board[r][0] == board[r][1] and board[r][0] == board[r][2]):
                return True
    
    for c in range(len(board[0])):
        if (board[0][c] != -1):
            if (board[0][c] == board[1][c] and board[0][c] == board[2][c]):
                return True

    return False

# 5. Write an algorithm which computes the number of trailing zeros in n factorial.
def factorial(n):
    if (n == 1):
        return 1
    return n * factorial(n-1)

def factorialZeros(n):
    fact = factorial(n)
    count = 0
    while (n%10 == 0):
        n = n/10
        count += 1
    return count

# 6. Given two arrays of integers, compute the pair of values (one value in each
# array) with the smallest (non-negative) difference. Return the difference.
def smallestDifference(A1, A2):
    diff = -1

    for num1 in A1:
        for num2 in A2:
            diff1 = num2 - num1
            diff2 = num1 - num2
            if (diff1 < 0 and diff2 < 0):
                continue
            else if (diff1 < 0):
                if (diff<0 or diff>diff2):
                    diff = diff2
            else if (diff2 < 0):
                if (diff<0 or diff>diff1):
                    diff = diff1
    return diff

# 7. Write a method that finds the maximum of two numbers. You should not use if-else
# or any other comparison operator.
def numberMax(m, n, i=0):
    if (m == i):
        return n
    if (n == i):
        return m
    
    return numberMax(m, n, i+1)

# 8. Given any integer, print an English phrase that describes the integer (e.g., "One Thousand,
# Two Hundred Thirty Four").
def englishInt(n):


# 9. Write methods to implement the multiply, subtract, and divide operations for integers.
# The results of all of these are integers. Use only the add operator.
def operations():


# 10. Given a list of people with their birth and death years, implement a method to
# compute the year with the most number of people alive. You may assume that all people were born
# between 1900 and 2000 (inclusive). If a person was alive during any portion of that year, they should
# be included in that year's count. For example, Person (birth= 1908, death= 1909) is included in the
# counts for both 1908 and 1909.
def livingPeople():
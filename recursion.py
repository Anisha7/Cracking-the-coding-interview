# 1. Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
# steps at a time. Implement a method to count how many possible ways the child can run up the
# stairs.

def tripleStep(n):
    memo = dict()
    for i in range(n+1):
        memo[i] = 0
    return tripleStepHelper(n, memo)

def tripleStepHelper(n, memo):
    if (n < 0):
        return 0
    if (n == 0):
        return 1
    # memoization for O(n) recursion
    if (memo[n] == 0):
        memo[n-1] = tripleStep(n-1)
        memo[n-2] = tripleStep(n-2)
        memo[n-3] = tripleStep(n-3)
        memo[n] = memo[n-1] + memo[n-2] + memo[n-3]
    return memo[n]

# 2. Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
# The robot can only move in two directions, right and down, but certain cells are "off limits" such that
# the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
# the bottom right.

# valid positions in grid G are more than -1 value
# less than or equal to -1 value are "off limit" cells
def robotGrid(G):
    if (len(G) == 0):
        return []
    rows = len(G)
    cols = len(G[0])
    return robotGridHelper(G, rows, cols)

def getPositions(G, rows, cols, pos):
    result = []
    # right, valid
    if (pos[1]+1 < cols and G[pos[0]][pos[1]+1] > -1):
        result += (pos[0], pos[1]+1)
    # bottom, valid
    if (pos[0]+1 < rows and G[pos[0]+1][pos[1]] > -1):
        result += (pos[0]+1, pos[1])

    return result

# pos = (r,c)
def robotGridHelper(G, rows, cols, pos=(0,0), result=[]):
    if (pos == (rows-1, cols-1)):
        return result
    
    positions = getPositions(G, rows, cols, pos)
    for posit in positions:
        solution = robotGridHelper(G,rows,cols,posit,result.append(posit))
        if (solution != None):
            return solution

    return None


# 3. Magic Index: A magic index in an array A [ 0 ••• n -1] is defined to be an index such that A[ i] =
# i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in
# array A.
# FOLLOW UP
# What if the values are not distinct?
    
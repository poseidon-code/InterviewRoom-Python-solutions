# PROBLEM: Rotting Oranges
# https://leetcode.com/problems/rotting-oranges/
# https://practice.geeksforgeeks.org/problems/rotten-oranges/0

from typing import List

# SOLUTION
def rot(grid: List[List[int]], i: int, j: int, d: int) -> int:
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[i]) or grid[i][j]!=1 : return 0
    grid[i][j] = d + 3
    return 1


def oranges (grid: List[List[int]]) -> int:
    fresh, d = 0, 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]==1 : fresh +=1
    
    old = fresh
    while fresh>0:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == d+2:
                    fresh -= rot(grid, i+1, j, d) +\
                             rot(grid, i-1, j, d) +\
                             rot(grid, i, j+1, d) +\
                             rot(grid, i, j-1, d)
        if fresh==old : return -1
        d+=1
        old=fresh

    return d


if __name__ == "__main__":
    # INPUT :
    grid = [[2,1,1],[1,1,0],[0,1,1]]

    # OUTPUT :
    print(oranges(grid))
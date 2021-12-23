# PROBLEM: Number of islands
# https://leetcode.com/problems/number-of-islands/
# https://practice.geeksforgeeks.org/problems/find-the-number-of-islands/1/?category[]=Graph&category[]=Graph&page=1&query=category[]Graphpage1category[]Graph

from typing import List

# SOLUTION
def dfs (grid: List[List[str]], i: int, j: int) -> int:
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[i]) or grid[i][j]=='0' : return 0
    
    grid[i][j] = '0'
    dfs(grid, i+1, j)
    dfs(grid, i-1, j)
    dfs(grid, i, j+1)
    dfs(grid, i, j-1)
    return 1


def oranges (grid: List[List[str]]) -> int:
    islands = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            islands += dfs(grid, i, j)
    
    return islands



if __name__ == "__main__":
    # INPUT :
    grid = [
        ['1','1','0','0','0'],
        ['1','1','0','0','0'],
        ['0','0','1','0','0'],
        ['0','0','0','1','1']
    ]

    # OUTPUT :
    print(oranges(grid))
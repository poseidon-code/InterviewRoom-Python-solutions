# PROBLEM: Region in binary matrix
# https://www.interviewbit.com/problems/region-in-binarymatrix/
# https://practice.geeksforgeeks.org/problems/length-of-largest-region-of-1s-1587115620/1


from typing import List

# SOLUTION
result = 0

def dfs(grid: List[List[int]], i: int, j: int):
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]==0 : return
    global result

    grid[i][j] = 0
    result+=1
    dfs(grid, i+1, j)
    dfs(grid, i-1, j)
    dfs(grid, i,   j+1)
    dfs(grid, i,   j-1)
    dfs(grid, i+1, j+1)
    dfs(grid, i-1, j+1)
    dfs(grid, i+1, j-1)
    dfs(grid, i-1, j-1)


def region (grid: List[List[int]]) -> int:
    n, m, maxarea = len(grid), len(grid[0]), 0
    global result

    for i in range(n):
        for j in range(m):
            result = 0
            if grid[i][j] == 1:
                dfs(grid, i, j)
                maxarea = max(maxarea, result)

    return maxarea


if __name__ == "__main__":
    # INPUT :
    grid = [[1,1,1,0],[0,0,1,0],[0,0,0,1]]

    # OUTPUT :
    print(region(grid))
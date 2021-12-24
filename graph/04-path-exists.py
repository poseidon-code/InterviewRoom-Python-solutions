# PROBLEM: Find whether the pat exists
# https://www.interviewbit.com/problems/path-in-directed-graph/
# https://practice.geeksforgeeks.org/problems/find-whether-path-exist5238/1/?category[]=Graph&category[]=Graph&page=1&query=category[]Graphpage1category[]Graph


from typing import List

# SOLUTION
def path (grid: List[List[int]], i: int, j: int) -> bool:
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[i]) or grid[i][j]==0 : return False
    if grid[i][j]==2 : return True
    grid[i][j] = 0

    return path(grid, i+1, j) or path(grid, i-1, j) or path(grid, i, j+1) or path(grid, i, j-1)


def is_possible (grid: List[List[int]]) -> bool:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                return path(grid, i, j)

    return False


if __name__ == "__main__":
    # INPUT :
    grid = [[1,3],[3,2]]

    # OUTPUT :
    print(is_possible(grid))
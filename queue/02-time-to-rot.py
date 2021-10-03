# PROBLEM: Minimum time to rot all oranges
# https://leetcode.com/problems/rotting-oranges/
# https://practice.geeksforgeeks.org/problems/rotten-oranges/0


from queue import Queue
from typing import List


# SOLUTION
def rotting(grid: List[List[int]]) -> int:
    q = Queue()
    dir = [[-1,0], [1,0], [0,-1], [0,1]]
    ct, result = 0, -1

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] > 0: ct+=1
            if grid[i][j] == 2: q.put([i,j])
    
    while q.empty()!=True:
        result+=1
        size=q.qsize()

        for k in range(size):
            cur = q.get()
            ct-=1

            for i in range(4):
                x = cur[0]+dir[i][0]
                y = cur[1]+dir[i][1]

                if x>=len(grid) or x<0 or y>=len(grid[0]) or y<0 or grid[x][y]!=1:
                    continue

                grid[x][y] = 2
                q.put([x, y])
    
    if ct==0: return max(0, result)
    return -1



if __name__ == "__main__":
    # INPUT :
    grid = [[2,1,1],[1,1,0],[0,1,1]]

    # OUTPUT :
    print(rotting(grid))
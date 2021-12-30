# PROBLEM: Snakes and Ladders
# https://leetcode.com/problems/snakes-and-ladders/
# https://www.interviewbit.com/problems/snake-ladder-problem/

from typing import List

# SOLUTION
def calc (row: int, next: int) -> List[int]:
    x, y = (next-1)//row, (next-1)%row
    if x%2==1 : y = row-1-y
    x = row-1-x
    return [x,y]


def snl (board: List[List[int]]) -> int:
    r = len(board)
    q = [1]
    step = 0

    while len(q)!=0:
        n = len(q)

        for i in range(n):
            t = q.pop()
            if t==r*r : return step

            for j in range(1,7):
                next_step = t+j
                if next_step>r*r : break

                v = calc(r, next_step)
                row, col = v[0], v[1]

                if board[row][col]!=-1:
                    next_step = board[row][col]

                if board[row][col]!=r*r+1:
                    q.append(next_step)
                    board[row][col]=r*r+1

        step+=1
    
    return -1



if __name__ == "__main__":
    # INPUT :
    board = [[-1,-1],[-1,3]]

    # OUTPUT :
    print(snl(board))
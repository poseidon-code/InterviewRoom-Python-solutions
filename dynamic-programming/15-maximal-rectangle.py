# PROBLEM: Maximal Rectangle
# https://leetcode.com/problems/maximal-rectangle/
# https://www.interviewbit.com/problems/max-rectangle-in-binary-matrix/

from typing import List

# SOLUTION
def rectangle (matrix: List[List[str]]) -> int:
    if len(matrix)==0 or len(matrix[0])==0 : return 0
    m, n, maxArea = len(matrix), len(matrix[0]), 0

    left, right, height = [0]*n, [n-1]*n, [0]*n

    for i in range(m):
        rB = n-1
        for j in range(n-1, -1, -1):
            if matrix[i][j] == '1':
                right[j] = min(right[j], rB)
            else:
                right[j] = n-1
                rB = j-1

        lB = 0
        for j in range(n):
            if matrix[i][j] == '1':
                left[j] = max(left[j], lB)
                height[j]+=1
                maxArea = max(maxArea, height[j] * (right[j] - left[j] + 1))
            else:
                height[j] = 0
                left[j] = 0
                lB = j+1
    
    return maxArea


if __name__ == "__main__":
    # INPUT :
    matrix = [
        ['1','0','1','0','0'],
        ['1','0','1','1','1'],
        ['1','1','1','1','1'],
        ['1','0','0','1','0']
    ]

    # OUTPUT :
    print(rectangle(matrix))
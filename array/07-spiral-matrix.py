# PROBLEM: Spiral matrix
# https://leetcode.com/problems/spiral-matrix/
# https://www.interviewbit.com/problems/spiral-order-matrix-i/


from typing import List

def spiral_matrix(matrix: List[List[int]]) -> List[int]:
    result = []
    m = len(matrix)
    n = len(matrix[0])
    directions = [[0,1],[1,0],[0,-1],[-1,0]]
    steps = [n, m-1]

    id = 0
    ir = 0
    ic = -1

    while steps[id%2]:
        for i in range(steps[id%2]):
            ir += directions[id][0]
            ic += directions[id][1]
            result.append(matrix[ir][ic])

        steps[id%2]-=1
        id = (id+1) % 4

    return result


if __name__ == "__main__":
    # INPUT :
    matrix = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ]

    # OUTPUT :
    print(spiral_matrix(matrix))
# PROBLEM: Matrix search
# https://leetcode.com/problems/search-a-2d-matrix/
# https://www.interviewbit.com/problems/matrix-search/


from typing import List

# SOLUTION
def matrix_search (matrix: List[List[int]], target: int) -> bool: 
    if len(matrix)==0 or len(matrix[0])==0 : return False

    m, n = len(matrix), len(matrix[0])
    start, end = 0, m*n-1

    while start <= end:
        mid = int(start + (end - start)/2)
        e = matrix[int(mid/n)][mid%n]

        if target < e : end = mid - 1
        elif target > e : start = mid + 1
        else : return True
    
    return False


if __name__ == "__main__":
    # INPUT :
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3

    # OUTPUT :
    print(matrix_search(matrix, target))
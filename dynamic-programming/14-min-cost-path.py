# PROBLEM: Min cost path
# https://www.interviewbit.com/problems/min-sum-path-in-matrix/ 


from typing import List

# SOLUTION
def path (A: List[List[int]]) -> int:
    m, n = len(A), len(A[0])
    dp = [[0]*n]*m

    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if i==m-1 and j==n-1 : dp[i][j] = A[i][j]
            elif i==m-1 : dp[i][j] = A[i][j] + dp[i][j+1]
            elif j==n-1 : dp[i][j] = A[i][j] + dp[i+1][j]
            else : dp[i][j] = A[i][j] + min(dp[i+1][j], dp[i][j+1])
    
    return dp[0][0]


if __name__ == "__main__":
    # INPUT :
    A = [[1,3,2],[4,3,1],[5,6,1]]

    # OUTPUT :
    print(path(A))
# PROBLEM: Burst Baloons (Matrix Chain Multiplication)
# https://leetcode.com/problems/burst-balloons/


from typing import List

# SOLUTION
def max_coins (nums: List[int]) -> int:
    N = [1] + [i for i in nums if i>0] + [1]
    n = len(N)

    dp = [[0]*n for _ in range(n)]

    for k in range(2, n):
        for l in range(0, n-k):
            r = l+k
            for i in range(l+1,r):
                dp[l][r] = max(dp[l][r], N[l] * N[i] * N[r] + dp[l][i] + dp[i][r])
    
    return dp[0][n - 1]


if __name__ == "__main__":
    # INPUT :
    nums = [3,1,5,8]

    # OUTPUT :
    print(max_coins(nums))
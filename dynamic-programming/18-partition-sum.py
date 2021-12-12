# PROBLEM: Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/

from typing import List

# SOLUTION
def partition (nums: List[int]) -> int:
    sum = 0
    for n in nums : sum += n
    if (sum & 1) == 1 : return False
    sum //= 2

    dp = [False] * (sum+1)
    dp[0] = True

    for x in nums:
        for i in range(sum, 0, -1):
            if i>= x:
                dp[i] = dp[i] or dp[i-x]
    
    return dp[sum]


if __name__ == "__main__":
    # INPUT :
    nums = [1,5,11,5]

    # OUTPUT :
    print(partition(nums))
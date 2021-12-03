# PROBLEM: Longest common substring
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/

from typing import List

# SOLUTION
def lcss (nums1: List[int], nums2: List[int]) -> int:
    m, n = len(nums1), len(nums2)
    dp = [0]*(n+1)
    result = 0

    for i in range(1, m+1):
        for j in range(n, 0, -1):
            if nums1[i-1] == nums2[j-1]:
                dp[j] = 1 + dp[j-1]
                result = max(result, dp[j])
            else:
                dp[j] = 0
    
    return result



if __name__ == "__main__":
    # INPUT :
    nums1 = [1,2,3,2,1]
    nums2 = [3,2,1,4,7]

    # OUTPUT :
    print(lcss(nums1, nums2))
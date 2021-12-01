# PROBLEM: Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/
# https://www.interviewbit.com/problems/longest-increasing-subsequence/


from typing import List

# SOLUTION
def lis (nums: List[int]) -> int:
    tails = [0]*len(nums)
    size = 0

    for x in nums:
        i, j = 0, size

        while i!=j:
            m = (i+j)//2
            if tails[m]<x : i = m+1
            else : j = m
        
        tails[i] = x
        if i==size : size+=1
    
    return size


if __name__ == "__main__":
    # INPUT :
    nums = [10,9,2,5,3,7,101,18]

    # OUTPUT :
    print(lis(nums))
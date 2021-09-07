# PROBLEM: Next permutation
# https://leetcode.com/problems/next-permutation/
# https://www.interviewbit.com/problems/next-permutation/


from typing import List


# SOLUTION
def next_permutation (nums: List[int]):
    n = len(nums)
    k=n-2
    l=n-1

    while k>=0:
        if nums[k] < nums[k+1]:
            break
        k-=1

    if k<0:
        nums.reverse()
    else:
        while l>k:
            if nums[l] > nums[k]:
                break
            l-=1
        
        nums[k], nums[l] = nums[l], nums[k]
        nums[k+1:] = nums[k+1:][::-1]


if __name__ == "__main__":
    # INPUT :
    nums = [1,1,5]

    # OUTPUT :
    next_permutation(nums)
    print(nums)